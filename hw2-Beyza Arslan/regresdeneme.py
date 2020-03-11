# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 02:49:02 2020

@author: Beyza
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

class LineerRegresyon:
    def __init__(self, w_intercept=True):
        self.coef_ = None
        self.intercept = w_intercept
        self.is_fit = False
        self.varss = None
    def fit(self, X, y):
        X = self.convert_to_array(X)
        y = self.convert_to_array(y)
        if self.intercept:
            X = self.add_intercept(X)
        temp_xtx = np.linalg.inv(np.dot(X.T,X))
        temp_xty = np.dot(X.T,y)
        self.coef_ = np.dot(temp_xtx,temp_xty)
        self.is_fit = True
        return self.coef_
    def convert_to_array(self, x):
        x = self.pandas_to_numpy(x)
        x = self.handle_1d_data(x)
        return x
    def pandas_to_numpy(self, x):
        if type(x) == type(pd.DataFrame()) or type(x) == type(pd.Series()):
            return x.values
        if type(x) == type(np.array([1, 2])):
            return x
        return np.array(x)
    def handle_1d_data(self, x):
        if x.ndim == 1:
            x = x.reshape(-1, 1)
        return x
    def add_intercept(self, X):
        rows = X.shape[0] 
        inter = np.ones(rows).reshape(-1,1)
        return np.hstack((X,inter))
    def predict(self, X):
        if not self.is_fit:
            raise ValueError("Please control fitness of function")
        X = self.convert_to_array(X)
        if self.intercept:
            X = self.add_intercept(X)
        return np.dot(X,self.coef_)
    
    def score(self, X, y):
        X = self.convert_to_array(X)
        y = self.convert_to_array(y)
        pred = self.predict(X)
        return np.mean((np.array(pred)-np.array(y))**2) 
    def residual(self,X,y):
        X = self.convert_to_array(X)
        y = self.convert_to_array(y)
        pred = self.predict(X)
        return np.array(y)-np.array(pred)
    def varyansofb(self,X):
        X = self.convert_to_array(X)
        temp_xtxx = np.linalg.inv(np.dot(X.T,X))
        temp_sigma = np.dot(e.T,e)/77
        return np.dot(temp_xtxx,temp_sigma)
    def tstat(self):
        SE = math.sqrt(lr.varyansofb(X))
        B = lr.coef_[0]
        tscore = (B-0)/SE
        if abs(tscore )> 1.96:
            return ('T-stat:' , abs(tscore[0]), 'so reject the hypothesis at the %5 significance level')
        else:
            return ("T-stat:" , abs(tscore[0]), "so can not reject the hypothesis at the %5 significance level")
    def interval(self):
        BB = float(lr.coef_[0])
        SE = float(math.sqrt(lr.varyansofb(X)))
        lower_limit = BB -1.96*SE
        upper_limit = BB + 1.96*SE
        return ('The %95 confidence interval for B1:' , lower_limit,upper_limit)
        
    
