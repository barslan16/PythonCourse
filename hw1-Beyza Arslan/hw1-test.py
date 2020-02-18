# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:19:27 2020

@author: Beyza
"""
import hw1

"""this part test the codes without exceptions and error
    please, see below for seeing error test"""

portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(5000.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
b = Stock(34, "ABA") #Create Stock with price 20 and symbol "ABA"
portfolio.buyStock(5, s) #Buys 5 shares of stock s
portfolio.buyStock(7, s) #Buys 7 shares of stock s
portfolio.buyStock(3, b)#Buys 3 shares of stock b
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
bf1 = BondFund("BHB") #Create BF  with symbol "BHB"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
portfolio.buyMutualFund(3, bf1) #Buys 3 shares of "BHB"
portfolio.sellStock(1,"ABA") #Sells 1 shares of "ABA"
portfolio.sellMutualFund(3,"BRT") #Sells 3 shares of BRT
portfolio.sellMutualFund(1,"BHB") #Sells 1 shares of BHB
portfolio.withdrawCash(500) #Removes 50$
print(portfolio) #Prints portfolio
portfolio.history() #Prints a list of all transactions ordered by time

""" For error test please see below, you can try separately
    some lines are became comment because they stop the program as the 
    code wants, The uncomment lines do not stop the program, they effect 
    history of transactions as you will see"""

portfolio = Portfolio() #Creates a new portfolio
#portfolio.addCash(-5000.50) #Test negative amount for adding cash
portfolio.addCash(5000.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
b = Stock(34, "ABA") #Create Stock with price 20 and symbol "ABA"
#portfolio.buyStock(-5, s) #Test for negative amount for buying stock
portfolio.buyStock(7, s) #Buys 7 shares of stock s
portfolio.buyStock(3, b)#Buys 3 shares of stock b
#portfolio.buyStock(3000000, b)#Test for buying stock by more money than cash
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
bf1 = BondFund("BHB") #Create BF  with symbol "BHB"
#portfolio.buyMutualFund(-10.3, mf1) #Test for negative amount for buying fund"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
#portfolio.buyMutualFund(2000000, mf2) #Test for buying fund by more money than cash 
portfolio.buyMutualFund(3, bf1) #Buys 3 shares of "BHB"
portfolio.sellStock(1,"HFH") #Sells 1 shares of "HFH"
portfolio.sellStock(1,"AA") #Test for selling stock that you did not have"
#portfolio.sellStock(-1,"HFH") #Test for negative amount for selling stock
#portfolio.sellMutualFund(-3,"BRT") #Test for negative amount for selling stock
portfolio.sellMutualFund(1,"BhB") #Test for selling fund that you did not have"
portfolio.sellMutualFund(1,"BHB") #Sells 3 shares of BRT
portfolio.sellMutualFund(3,"BRT") #Sells 3 shares of BRT
portfolio.withdrawCash(500) #Removes 50$
#portfolio.withdrawCash(-500) #Test negative amount for removing
#portfolio.withdrawCash(500000) #Test for remove more money than cash
print(portfolio) #Prints portfolio
portfolio.history() #Prints a list of all transactions ordered by time


      