# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:03:04 2020

@author: Beyza
"""

def binarify(num): 
  """convert positive integer to base 2"""
  
  digits = []
  while True:
      if num%2 == 0:
          digits.append("0")
          num = num//2
      elif num%2 == 1:
          digits.append("1")
          num = num//2
      if num == 0:
          return "".join(digits[::-1])
      if num <0:
          return "0"
          
      
   
def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  digits = []
  while True:
      if num%base == 0:
          digits.append("0")
          num = num//base
      elif num <0:
          return "0"
      else:
          digits.append(str(num%base))
          num = num//base
      if num == 0:
         return "".join(digits[::-1]) 
          

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  a = len(string)
  string = string[::-1]
  result = 0
  for i in range(a):
      result += int(string[i])*base**i
  return result
      
 

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  a = base_to_int(str1,base1)
  b = base_to_int(str2,base2)
  tmp = a+b
  result = int_to_base(tmp, base1)
  return result 

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  a = base_to_int(str1,base1)
  b = base_to_int(str2,base2)
  tmp = a*b
  result = int_to_base(tmp, base1)
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
  rom = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
  result = []
  if num > 3999 or num < 0:
      raise ValueError
  for i in range(len(ints)):
        count = num // ints[i]
        result.append(rom[i] * count)
        num -= ints[i] * count
  
  return ''.join(result)