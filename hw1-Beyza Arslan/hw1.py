# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 00:24:33 2020

@author: Beyza
"""

import random
import datetime

class Stock(object):
    def __init__(self,stock_price,stock_name):
        self.stock = {}
        self.stock_name = stock_name
        self.stock_price = stock_price
        self.stock.update({self.stock_name:self.stock_price})              
class MutualFund(object):
    def __init__(self,mf_name):
        self.mutualfund = []
        self.mf_name = mf_name
        self.mutualfund.append(mf_name)
class BondFund(MutualFund):
    def createbond(self):
        self.bond = []
    def __str__(self):
        return self.bond
    def __main__(self):
        return self.bond
        
        

class Portfolio():
    def __init__(self):
        self.stock_pocket = {}
        self.stock_price_list = {}
        self.stockpocketlist = []
        self.mutualfund_pocket = {}
        self.mutualfundlist = []
        self.bondfundlist = []
        self.bondfund_pocket = {}
        self.history_list = []
        self.cash_pocket = 0
    def addCash(self,amount):
        if amount <= 0:
            raise ValueError ("You can not add negative amount as a cash")
        self.cash_pocket += amount 
        self.history_list.append(str(datetime.date.today())+":"+ " " + str(amount) + "$" + " "+ "cash" +" "+ "is added")
    def withdrawCash(self,amount):
        if amount <=0:
            raise ValueError ("You can not withdraw negative amount as a cash")
        if amount > self.cash_pocket:
            raise RuntimeError ("You do not have enough cash, please check your portfolio" + "\n" + portfolio.__str__())
        self.cash_pocket -= amount
        self.history_list.append(str(datetime.date.today())+":"+ " "+str(amount) + "$" + " "+ "cash" + " " + "is withdrawn")
    def buyStock(self, amount, s):
        if amount <= 0:
            raise ValueError ("You need to enter positive value for an amount")
        if amount*s.stock_price > self.cash_pocket:
            raise RuntimeError ("You do not have enough cash, please check your portfolio" + "\n" + portfolio.__str__()) 
        self.cash_pocket -= amount*s.stock_price
        x = s.stock_name
        if s.stock_name in self.stockpocketlist:
            self.stock_pocket[s.stock_name] =  self.stock_pocket[s.stock_name] + amount
        else:
            self.stock_pocket.update({s.stock_name:amount}) 
            self.stockpocketlist.append(x) 
            self.stock_price_list.update({s.stock_name:s.stock_price})
        self.history_list.append(str(datetime.date.today())+":"+ " "+str(amount) + " "+ s.stock_name + " "+ "is purchased" + " " + "as a stock" + " " + "by" + " " +str(amount*s.stock_price)+"$")
    def buyMutualFund(self,amount,mf):
        if amount <= 0:
            raise ValueError ("You need to enter positive value for an amount")
        if amount > self.cash_pocket:
            raise RuntimeError ("You do not have enough cash, please check your portfolio" + "\n" + portfolio.__str__()) 
        self.cash_pocket -= amount
        a = isinstance(mf,BondFund)
        if a == True:
            self.bondfund_pocket.update({mf.mf_name:amount})
            self.history_list.append(str(datetime.date.today())+":"+ " "+ str(amount)+ " " + mf.mf_name + " "+ "is purchased" + " " + "as a bondfund" + " " + "by" + " " +str(amount)+"$")
            x = mf.mf_name
            self.bondfundlist.append(x)
        else:
            self.mutualfund_pocket.update({mf.mf_name:amount})
            self.history_list.append(str(datetime.date.today()) +":"+ " "+ str(amount) + " "+ mf.mf_name + " "+ "is purchased"+ " " + "as a mutualfund" + " " + "by" + " " +str(amount)+"$")
            y = mf.mf_name
            self.mutualfundlist.append(y)
        
    def sellStock(self,amount,stock_name):
        if amount <= 0:
            raise ValueError ("You need to enter positive value for an amount")
        r1 = random.uniform(0.5,1.5)
        try:
            if amount > self.stock_pocket[stock_name]:
                raise RuntimeError ("you do not have enough stock, please check your portfolio" + "\n" + portfolio.__str__())
            else:
                self.cash_pocket += round(amount*r1*self.stock_price_list[stock_name])
                self.stock_pocket[stock_name] -= amount
                self.history_list.append(str(datetime.date.today())+":"+ " "+str(amount)+ " " + s.stock_name + " "+ "is sold" + " " + "from your stock" + " " + "by" + " " +  str(round(amount*r1*self.stock_price_list[stock_name],3)) + "$")
        except KeyError:
            self.history_list.append("You do not have a stock that is named:" + " " + stock_name )
        except RuntimeError:
            self.history_list.append("You entered invalid amount for stock selling")
    def sellMutualFund(self,amount,mf_name):
        if amount <= 0:
            raise ValueError ("You need to enter positive value for an amount")
        r2 = random.uniform(0.9,1.2)
        if mf_name in self.bondfundlist:
            try:
                if amount > self.bondfund_pocket[mf_name]:
                    raise RuntimeError ("You do not have enough bondfund, please check your portfolio" + "\n"+ portfolio.__str__())
                else:
                    self.cash_pocket -= amount*r2
                    self.bondfund_pocket[mf_name] -= amount
                    self.history_list.append(str(datetime.date.today())+":"+ " "+str(amount) + " "+ mf_name + " "+ "is sold" + " " + "from your bondfund" + " " + "by" + " " +  str(round(amount*r2,3)) + "$")
            except RuntimeError:
                self.history_list.append("You entered invalid amount for bond fund")
            except KeyError:
                self.history_list.append("You do not have a bondfund that is named:" + mf_name)
        else:
            try:
                if amount > self.mutualfund_pocket[mf_name]:
                    raise RuntimeError ("You do not have enough mutualfund, please check your portfolio"  + "\n"+ portfolio.__str__())
                else:
                    self.cash_pocket -= round(amount*r2,3)
                    self.mutualfund_pocket[mf_name] -= amount
                    self.history_list.append(str(datetime.date.today())+":"+" "  + str(amount)+" " + mf_name+" " + "is sold" + " " + "from your mutualfund" + " " + "by" + " " +  str(round(amount*r2,3)) + "$")
            except RuntimeError:
                self.history_list.append("You entered invalid amount for mutual fund")
            except KeyError:
                self.history_list.append("You do not have a mutualfund that is named:" + mf_name)
    def history(self):
        print("A historical list of your all transactions")
        for t in self.history_list:
            print (t + "\n " + "********************************************************")
        print("Cash:" + " " + str(round(self.cash_pocket,3)) + "$")

    def __str__(self):
        return "Your portfolio is:" + "\n"+ "-----------------------------------" + "\n"+ "Cash:" + str(round(self.cash_pocket,3)) +"$"+ "\n"+ "Stock:" + str(self.stock_pocket) + "\n"+ "MutualFund:" + str(self.mutualfund_pocket) + "\n" + "BondFund:" + str(self.bondfund_pocket) + "\n" + "-----------------------------------"
    
    
        
            
            
            
      
        
        
        