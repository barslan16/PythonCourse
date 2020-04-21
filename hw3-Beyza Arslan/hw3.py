# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:33:09 2020

@author: beyza
"""

# I created four different models. Because I could not use two counties in one model. I constructed seperated models for each.
# You can find my answer end of this file.

import pandas as pd
import numpy as np
import pystan
import matplotlib



# First Model: Uninformative prior with country-county [b1 ~ normal (0, 1)]

data = pd.read_csv('C:\\Users\\beyza\\Documents\\dersler\\qmbu450\\hw3-Beyza Arslan\\trend2.csv')
data = data.dropna()

data.county= data.country.str.strip()
mn_counties = data.county.unique()

county_lookup = dict(zip(mn_counties, range(len(mn_counties))))

county = data['county_code'] = data.county.replace(county_lookup).values

data.outcome = data.church2

gini = data.gini_net.values
rgdpl = data.rgdpl.values
church2 = data.church2.values
n_county = data.country.unique()

varying_intercept_model1 = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> county[N];
  vector[N] x;
  vector[N] z;
  vector[N] y;
} 
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] <- a[county[i]]  + x[i]*b1 + z[i]*b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 1);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_data_model1 = {'N': len(church2),
                                 'J': len(n_county),
                                 'county': county+1,
                                 'x': gini,
                                 'y': church2,
                                 'z': rgdpl}

varying_intercept_fit_model1 = pystan.stan(model_code=varying_intercept_model1, data=varying_intercept_data_model1, iter=1000, chains=2)
varying_intercept_fit_model1

# Second Model: Uninformative prior with year-county [b1 ~ normal (0, 1)]

data = pd.read_csv('C:\\Users\\beyza\\Documents\\dersler\\qmbu450\\hw3-Beyza Arslan\\trend2.csv')
data = data.dropna()

data.county = data.year
mn_counties = data.county.unique()

county_lookup = dict(zip(mn_counties, range(len(mn_counties))))

county = data['county_code'] = data.county.replace(county_lookup).values

data.outcome = data.church2

gini = data.gini_net.values
rgdpl = data.rgdpl.values
church2 = data.church2.values
n_county = data.year.unique()

varying_intercept_model2 = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> county[N];
  vector[N] x;
  vector[N] z;
  vector[N] y;
} 
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] <- a[county[i]]  + x[i]*b1 + z[i]*b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 1);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_data_model2 =  {'N': len(church2),
                                  'J': len(n_county),
                                  'county': county+1,
                                  'x': gini,
                                  'y': church2,
                                  'z': rgdpl}

varying_intercept_fit_model2 = pystan.stan(model_code=varying_intercept_model2, data=varying_intercept_data_model2, iter=1000, chains=2)
varying_intercept_fit_model2

# Third Model: Informative prior with country-county [b1 ~ normal (0, 100)]

data = pd.read_csv('C:\\Users\\beyza\\Documents\\dersler\\qmbu450\\hw3-Beyza Arslan\\trend2.csv')
data = data.dropna()

data.county= data.country.str.strip()
mn_counties = data.county.unique()

county_lookup = dict(zip(mn_counties, range(len(mn_counties))))

county = data['county_code'] = data.county.replace(county_lookup).values

data.outcome = data.church2

gini = data.gini_net.values
rgdpl = data.rgdpl.values
church2 = data.church2.values
n_county = data.country.unique()

varying_intercept_model3 = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> county[N];
  vector[N] x;
  vector[N] z;
  vector[N] y;
} 
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] <- a[county[i]]  + x[i]*b1 + z[i]*b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 100);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_data_model3 =  {'N': len(church2),
                                  'J': len(n_county),
                                  'county': county+1,
                                  'x': gini,
                                  'y': church2,
                                  'z': rgdpl}

varying_intercept_fit_model3 = pystan.stan(model_code=varying_intercept_model3, data=varying_intercept_data_model3, iter=1000, chains=2)
varying_intercept_fit_model3

# Fourth Model: Informative prior with year-county [b1 ~ normal (0, 100)]

data = pd.read_csv('C:\\Users\\beyza\\Documents\\dersler\\qmbu450\\hw3-Beyza Arslan\\trend2.csv')
data = data.dropna()

data.county = data.year
mn_counties = data.county.unique()

county_lookup = dict(zip(mn_counties, range(len(mn_counties))))

county = data['county_code'] = data.county.replace(county_lookup).values

data.outcome = data.church2

gini = data.gini_net.values
rgdpl = data.rgdpl.values
church2 = data.church2.values
n_county = data.year.unique()

varying_intercept_model4 = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> county[N];
  vector[N] x;
  vector[N] z;
  vector[N] y;
} 
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] <- a[county[i]]  + x[i]*b1 + z[i]*b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 100);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_data_model4 = {'N': len(church2),
                          'J': len(n_county),
                          'county': county+1,
                          'x': gini,
                          'y': church2,
                          'z': rgdpl}

varying_intercept_fit_model4 = pystan.stan(model_code=varying_intercept_model4, data=varying_intercept_data_model4, iter=1000, chains=2)
varying_intercept_fit_model4

#All graphics
varying_intercept_fit_model1.plot()
varying_intercept_fit_model2.plot()
varying_intercept_fit_model3.plot()
varying_intercept_fit_model4.plot()



# Coefficients for the main Betas in the models are here:
## 1. First Model: 0.29
## 2. Second Model: 0.82
## 3. Third Model: 0.33
## 4. Forth Model: 0.89
## If we increase the variances in the normal distributions of the prior, Beta values in the model also increase.