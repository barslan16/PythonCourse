# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:57:09 2020

@author: Beyza
"""

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

#the all 3 codes are copied and pasted below the page because the code need to get some variables into their memory    
url2 = "https://apps.who.int/gho/athena/data/GHO/EQ_INFANTMORT.html?profile=ztable&filter=COUNTRY:*;REGION:*;WEALTHQUINTILE:-;RESIDENCEAREATYPE:-;DATASOURCE:*"

r = requests.get(url2)
soup = BeautifulSoup(r.text,"html.parser")
GHO = ""
PublishState = ""
Year = ""
Region = ""
Country = ""
DisplayValue = ""
NumbericValue = ""

table = soup.findAll("tr")[1:]

ülkes = []
ölüm = []

for rows in table:
    cells = rows.findAll("td")
    if len(rows) > 0:
        Year = cells[3].find(text = True)     
        Country = cells[5].find(text = True)
        NumbericValue = cells[7].find(text = True)
        if Country in ülkes:
            ülkes[-1] = Country
            ölüm[-1]=NumbericValue
            pass
        else:
             ülkes.append(Country)
             ölüm.append(NumbericValue)
            
url = "https://apps.who.int/gho/athena/data/GHO/MDG_0000000003.html?profile=ztable&filter=COUNTRY:*;REGION:*"

r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
GHO = ""
PublishState = ""
Year = ""
Region = ""
Country = ""
DisplayValue = ""
NumbericValue = ""

table1 = soup.findAll("tr")[1:]

ülke = []
doğum = []

for rows in table1:
    cells = rows.findAll("td")
    if len(rows) > 0:
        Year = cells[2].find(text = True)     
        Country = cells[4].find(text = True)
        NumbericValue = cells[6].find(text = True)
        if Country in ülkes:
            ülke.append(Country)
            doğum.append(NumbericValue)
            
url3 = "https://apps.who.int/gho/athena/data/GHO/EQ_ANC.html?profile=ztable&filter=COUNTRY:*;REGION:*;EDUCATIONLEVEL:-;WEALTHQUINTILE:-;RESIDENCEAREATYPE:-;DATASOURCE:*"

r = requests.get(url3)
soup = BeautifulSoup(r.text,"html.parser")
GHO = ""
PublishState = ""
Year = ""
Region = ""
Country = ""
DisplayValue = ""
NumbericValue = ""

table3 = soup.findAll("tr")[1:]

ülkess = []
care = []

for rows in table3:
    cells = rows.findAll("td")
    if len(rows) > 0:
        GHO = cells[0].find(text=True)
        Year = cells[3].find(text = True)     
        Country = cells[5].find(text = True)
        NumbericValue = cells[7].find(text = True)
        if Country in ülkess:
            ülkess[-1] = Country
            care[-1] = NumbericValue
            pass
        else:
            if Country in ülkes and Country in ülke:
                ülkess.append(Country)
                care.append(NumbericValue)
                
url2 = "https://apps.who.int/gho/athena/data/GHO/EQ_INFANTMORT.html?profile=ztable&filter=COUNTRY:*;REGION:*;WEALTHQUINTILE:-;RESIDENCEAREATYPE:-;DATASOURCE:*"

r = requests.get(url2)
soup = BeautifulSoup(r.text,"html.parser")
GHO = ""
PublishState = ""
Year = ""
Region = ""
Country = ""
DisplayValue = ""
NumbericValue = ""

table = soup.findAll("tr")[1:]

ülkes = []
ölüm = []

for rows in table:
    cells = rows.findAll("td")
    if len(rows) > 0:
        Year = cells[3].find(text = True)     
        Country = cells[5].find(text = True)
        NumbericValue = cells[7].find(text = True)
        if Country in ülkes:
            ülkes[-1] = Country
            ölüm[-1]=NumbericValue
            pass
        else:
            if Country in ülke and Country in ülkess:
               ülkes.append(Country)
               ölüm.append(NumbericValue)
            
url = "https://apps.who.int/gho/athena/data/GHO/MDG_0000000003.html?profile=ztable&filter=COUNTRY:*;REGION:*"

r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
GHO = ""
PublishState = ""
Year = ""
Region = ""
Country = ""
DisplayValue = ""
NumbericValue = ""

table1 = soup.findAll("tr")[1:]

ülke = []
doğum = []

for rows in table1:
    cells = rows.findAll("td")
    if len(rows) > 0:
        Year = cells[2].find(text = True)     
        Country = cells[4].find(text = True)
        NumbericValue = cells[6].find(text = True)
        if Country in ülkes and Country in ülkess:
            ülke.append(Country)
            doğum.append(NumbericValue)
            
url3 = "https://apps.who.int/gho/athena/data/GHO/EQ_ANC.html?profile=ztable&filter=COUNTRY:*;REGION:*;EDUCATIONLEVEL:-;WEALTHQUINTILE:-;RESIDENCEAREATYPE:-;DATASOURCE:*"

r = requests.get(url3)
soup = BeautifulSoup(r.text,"html.parser")
GHO = ""
PublishState = ""
Year = ""
Region = ""
Country = ""
DisplayValue = ""
NumbericValue = ""

table3 = soup.findAll("tr")[1:]

ülkess = []
care = []

for rows in table3:
    cells = rows.findAll("td")
    if len(rows) > 0:
        GHO = cells[0].find(text=True)
        Year = cells[3].find(text = True)     
        Country = cells[5].find(text = True)
        NumbericValue = cells[7].find(text = True)
        if Country in ülkess:
            ülkess[-1] = Country
            care[-1] = NumbericValue
            pass
        else:
            if Country in ülkes and Country in ülke:
                ülkess.append(Country)
                care.append(NumbericValue)


adolescent_birth = pd.Series(doğum,index=ülke,name="Birth")
infant_mortality = pd.Series(ölüm,index=ülke, name="Death")
antenatal_care = pd.Series(care,index=ülke, name= "Care")
df = pd.concat([infant_mortality,adolescent_birth,antenatal_care], axis=1)
df.to_csv("infantmortality.csv")

import regresdeneme

df = pd.read_csv("infantmortality.csv")
df.head()
s1 = pd.Series(df["Care"])
s2 = pd.Series(df["Death"])
new_frame = pd.concat(objs=(s1 , s2), axis=1)
new_frame = new_frame.astype(int)

train_df = new_frame[0:int((len(new_frame)*70)/100)]
test_df = new_frame[int((len(new_frame)*70)/100):len(new_frame)]

X = train_df["Care"]
y = train_df["Death"]
lr = LineerRegresyon(w_intercept=True)
lr.fit(X,y)
print(lr.coef_)
print(lr.predict([65]))

X = pd.Series(test_df["Care"])
y = lr.predict(test_df["Care"]).tolist()
test_df.plot.scatter(x="Care", y="Death")
plt.plot(X,y,color="green")

scores = lr.score(train_df["Care"],train_df["Death"])

e = lr.residual(train_df["Care"],train_df["Death"])

varb = lr.varyansofb(train_df["Care"])
print(math.sqrt(varb))

tstatt = lr.tstat()
print(tstatt)

inter = lr.interval()
print(inter)




            
