# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:03:28 2020

@author: beyza
"""


# quandl for financial data
import quandl
# pandas for data manipulation
import pandas as pd
quandl.ApiConfig.api_key = 'JZpMtR4eEN3LyBqXMwNR'
# Retrieve TSLA data from Quandl
tesla = quandl.get('WIKI/TSLA')
gm = quandl.get('WIKI/GM')

#tsla = pd.read_csv('TSLA.csv')

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import numpy as np
import datetime
from fbprophet.plot import plot_yearly
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error



plt.plot(tesla.index, tesla['Adj. Close'], 'r')
plt.title('Tesla Stock Price')
plt.ylabel('Price ($)');
plt.show();

# Yearly average number of shares outstanding for Tesla and GM
tesla_shares = {2018: 168e6, 2017: 162e6, 2016: 144e6, 2015: 128e6, 2014: 125e6, 2013: 119e6, 2012: 107e6, 2011: 100e6, 2010: 51e6}
gm_shares = {2018: 1.42e9, 2017: 1.50e9, 2016: 1.54e9, 2015: 1.59e9, 2014: 1.61e9, 2013: 1.39e9, 2012: 1.57e9, 2011: 1.54e9, 2010:1.50e9}

# Create a year column 
tesla['Year'] = tesla.index.year

# Take Dates from index and move to Date column 
tesla.reset_index(level=0, inplace = True)
tesla['cap'] = 0

# Calculate market cap for all years
for i, year in enumerate(tesla['Year']):
    # Retrieve the shares for the year
    shares = tesla_shares.get(year)
    # Update the cap column to shares times the price
    tesla.loc[i, 'cap'] = shares * tesla.loc[i, 'Adj. Close']

# Create a year column 
gm['Year'] = gm.index.year

# Take Dates from index and move to Date column 
gm.reset_index(level=0, inplace = True)
gm['cap'] = 0

# Calculate market cap for all years
for i, year in enumerate(gm['Year']):
    # Retrieve the shares for the year
    shares = gm_shares.get(year)
    
    # Update the cap column to shares times the price
    gm.loc[i, 'cap'] = shares * gm.loc[i, 'Adj. Close']
    
# Merge the two datasets and rename the columns
cars = gm.merge(tesla, how='inner', on='Date')
cars.rename(columns={'cap_x': 'gm_cap', 'cap_y': 'tesla_cap'}, inplace=True)

# Select only the relevant columns
cars = cars.loc[:, ['Date', 'gm_cap', 'tesla_cap']]

# Divide to get market cap in billions of dollars
cars['gm_cap'] = cars['gm_cap'] / 1e9
cars['tesla_cap'] = cars['tesla_cap'] / 1e9
    
plt.figure(figsize=(10, 8))
plt.plot(cars['Date'], cars['tesla_cap'], 'r-', label = 'TESLA')
plt.xlabel('Date'); plt.ylabel('Market Cap (Billions $)'); plt.title('Market Cap of Tesla')
plt.legend();

import fbprophet

# Prophet requires columns ds (Date) and y (value)
tesla =tesla.rename(columns={'Date': 'ds', 'cap': 'y'})
# Put market cap in billions
tesla['y'] = tesla['y'] / 1e9

# Make the prophet models and fit on the data
# changepoint_prior_scale can be changed to achieve a better fit
tesla_prophet = fbprophet.Prophet(changepoint_prior_scale=0.15, n_changepoints=20)
tesla_prophet.fit(tesla);

# Make a future dataframe for 3 years
tesla_forecast = tesla_prophet.make_future_dataframe(periods=365*1, freq='D')
# Make predictions
tesla_forecast = tesla_prophet.predict(tesla_forecast)

tesla_prophet.plot(tesla_forecast, xlabel = 'Date', ylabel = 'Market Cap (billions $)')
plt.title('Market Cap of Tesla');

fig1 = tesla_prophet.plot_components(tesla_forecast)


# Try 4 different changepoints
for changepoint in [0.001, 0.05, 0.1, 0.5]:
    model = fbprophet.Prophet(daily_seasonality=False, changepoint_prior_scale=changepoint)
    model.fit(tesla)
    
    future = model.make_future_dataframe(periods=365, freq='D')
    future = model.predict(future)
    
    tesla[changepoint] = future['yhat']
    
# Load in the data     
elonmusk_search = pd.read_csv('elonmusk_search.csv')

# Convert month to a datetime
elonmusk_search['Month'] = pd.to_datetime(elonmusk_search['Month'])
tesla_changepoints = [date for date in tesla_prophet.changepoints]

plt.plot(elonmusk_search['Month'], elonmusk_search['Search'], label = 'Searches')

# Plot the changepoints
plt.vlines(tesla_changepoints, ymin = 0, ymax= 100, colors = 'r', linewidth=1, linestyles = 'dashed', label = 'Changepoints')
plt.ylabel('Relative Search Freq'); plt.legend()
plt.title('Elon Musk Search Terms and Changepoints');

# Load in the data 
brentoil_price = pd.read_csv('brent_oil_future.csv')

# Convert month to a datetime
brentoil_price['x'] = pd.to_datetime(brentoil_price['x'])
tesla_changepoints = [date for date in tesla_prophet.changepoints]

plt.plot(brentoil_price['x'], brentoil_price['x.1'], label = 'Prices')

# Plot the changepoints
plt.vlines(tesla_changepoints, ymin = 0, ymax= 150, colors = 'r', linewidth=1, linestyles = 'dashed', label = 'Changepoints')
plt.ylabel('Relative Prices'); plt.legend()
plt.title('Brent Oil Prices and Changepoints');

# Load in the data 
sp_500 = pd.read_csv('^GSPC.csv')

# Convert month to a datetime
sp_500['Date'] = pd.to_datetime(sp_500['Date'])
tesla_changepoints = [date for date in tesla_prophet.changepoints]

plt.plot(sp_500['Date'], sp_500['Adj Close'], label = 'Values')

# Plot the changepoints
plt.vlines(tesla_changepoints, ymin = 0, ymax= 3000, colors = 'r', linewidth=1, linestyles = 'dashed', label = 'Changepoints')
plt.ylabel('Relative Values'); plt.legend()
plt.title('S&P 500 and Changepoints');


#with additional regressor (elonmusk search terms)
tsla = pd.read_csv('TSLA.csv')
elonmusk_searchh = pd.read_csv('elonmusk_search.csv')

train_dataset= pd.DataFrame()
train_dataset['ds'] = pd.to_datetime(tsla["Date"])
train_dataset['y']=tsla["Adj Close"]

train_dataset["search"] = elonmusk_searchh["Search"]


train_x = train_dataset[:30]
test_x = train_dataset[30:]

pro_regressor = fbprophet.Prophet(changepoint_prior_scale=0.15, n_changepoints=20)

pro_regressor.add_regressor('search')

pro_regressor.add_regressor('value')

pro_regressor.fit(train_x)

future_data = pro_regressor.make_future_dataframe(periods=249)

forecast_data = pro_regressor.predict(test_x)

metric_tesla = forecast_data.set_index('ds')[['yhat']].join(test_x.set_index('ds').y).reset_index()

metric_tesla.dropna(inplace=True)

r2_score(metric_tesla.y, metric_tesla.yhat)

mean_squared_error(metric_tesla.y, metric_tesla.yhat)

mean_absolute_error(metric_tesla.y, metric_tesla.yhat)

#with additional regressor (sp500 values)

sp_500 = pd.read_csv('^GSPC.csv')

train_dataset= pd.DataFrame()
train_dataset['ds'] = pd.to_datetime(tsla["Date"])
train_dataset['y']=tsla["Adj Close"]

train_dataset["value"] = sp_500["Adj Close"]

train_x = train_dataset[:30]
test_x = train_dataset[30:]

pro1_regressor = fbprophet.Prophet(changepoint_prior_scale=0.15, n_changepoints=20)

pro1_regressor.add_regressor('value')

pro1_regressor.fit(train_x)

future1_data = pro1_regressor.make_future_dataframe(periods=249)
forecast1_data = pro1_regressor.predict(test_x)
metric1_tesla = forecast1_data.set_index('ds')[['yhat']].join(test_x.set_index('ds').y).reset_index()
metric1_tesla.dropna(inplace=True)

r2_score(metric1_tesla.y, metric1_tesla.yhat)

mean_squared_error(metric1_tesla.y, metric1_tesla.yhat)

mean_absolute_error(metric1_tesla.y, metric1_tesla.yhat)

#with additional regressor only brent oil prices
brentoil_pricee = pd.read_csv('brent_oil_future.csv')

train_dataset= pd.DataFrame()
train_dataset['ds'] = pd.to_datetime(tsla["Date"])
train_dataset['y']=tsla["Adj Close"]

train_dataset["price"] = brentoil_pricee["x.1"]

train_x = train_dataset[:30]
test_x = train_dataset[30:]

pro4_regressor = fbprophet.Prophet(changepoint_prior_scale=0.15, n_changepoints=20)

pro4_regressor.add_regressor('price')

pro4_regressor.fit(train_x)

future4_data = pro4_regressor.make_future_dataframe(periods=249)
forecast4_data = pro4_regressor.predict(test_x)
metric4_tesla = forecast4_data.set_index('ds')[['yhat']].join(test_x.set_index('ds').y).reset_index()
metric4_tesla.dropna(inplace=True)

r2_score(metric4_tesla.y, metric4_tesla.yhat)

mean_squared_error(metric4_tesla.y, metric4_tesla.yhat)

mean_absolute_error(metric4_tesla.y, metric4_tesla.yhat)

#with additional regressor both value and search
train_dataset= pd.DataFrame()
train_dataset['ds'] = pd.to_datetime(tsla["Date"])
train_dataset['y']=tsla["Adj Close"]

train_dataset["search"] = elonmusk_searchh["Search"]
train_dataset["value"] = sp_500["Adj Close"]

train_x = train_dataset[:30]
test_x = train_dataset[30:]

pro2_regressor = fbprophet.Prophet(changepoint_prior_scale=0.15, n_changepoints=20)
pro2_regressor.add_regressor('value')
pro2_regressor.add_regressor('search')

pro2_regressor.fit(train_x)

future2_data = pro2_regressor.make_future_dataframe(periods=249)

forecast2_data = pro2_regressor.predict(test_x)
metric2_tesla = forecast2_data.set_index('ds')[['yhat']].join(test_x.set_index('ds').y).reset_index()
metric2_tesla.dropna(inplace=True)
r2_score(metric2_tesla.y, metric2_tesla.yhat)
mean_squared_error(metric2_tesla.y, metric2_tesla.yhat)
mean_absolute_error(metric2_tesla.y, metric2_tesla.yhat)

#with additional regressor price, value and search

train_dataset= pd.DataFrame()
train_dataset['ds'] = pd.to_datetime(tsla["Date"])
train_dataset['y']=tsla["Adj Close"]

train_dataset["search"] = elonmusk_searchh["Search"]
train_dataset["value"] = sp_500["Adj Close"]
train_dataset["price"] = brentoil_pricee["x.1"]


train_x = train_dataset[:30]
test_x = train_dataset[30:]

pro5_regressor = fbprophet.Prophet(changepoint_prior_scale=0.15, n_changepoints=20)
pro5_regressor.add_regressor('value')
pro5_regressor.add_regressor('search')
pro5_regressor.add_regressor('price')

pro5_regressor.fit(train_x)

future5_data = pro5_regressor.make_future_dataframe(periods=365*6)

forecast5_data = pro5_regressor.predict(test_x)
metric5_tesla = forecast5_data.set_index('ds')[['yhat']].join(test_x.set_index('ds').y).reset_index()
metric5_tesla.dropna(inplace=True)
r2_score(metric5_tesla.y, metric5_tesla.yhat)
mean_squared_error(metric5_tesla.y, metric5_tesla.yhat)
mean_absolute_error(metric5_tesla.y, metric5_tesla.yhat)

#regression with no item

train_dataset= pd.DataFrame()
train_dataset['ds'] = pd.to_datetime(tsla["Date"])
train_dataset['y']=tsla["Adj Close"]

train_x = train_dataset[:30]
test_x = train_dataset[30:]

pro3_regressor = fbprophet.Prophet(changepoint_prior_scale=0.15, n_changepoints=20)
pro3_regressor.fit(train_x)

future3_data = pro3_regressor.make_future_dataframe(periods=249)
forecast3_data = pro3_regressor.predict(test_x)

metric3_tesla = forecast3_data.set_index('ds')[['yhat']].join(test_x.set_index('ds').y).reset_index()
metric3_tesla.dropna(inplace=True)
r2_score(metric3_tesla.y, metric3_tesla.yhat)
mean_squared_error(metric3_tesla.y, metric3_tesla.yhat)
mean_absolute_error(metric3_tesla.y, metric3_tesla.yhat)