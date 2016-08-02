# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:49:46 2016

@author: HJohnson

2520 is the smallest number that can be divided by each
 of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
 by all of the numbers from 1 to 20?
 
"""

def isDivisible(n):
   for i in range(1,21):
       a = n % i
       if (a != 0):
           return False
   return True
           



for i in range(1,999999999):
    if isDivisible(i):
        print(i)
        break
    
    # 232792560

