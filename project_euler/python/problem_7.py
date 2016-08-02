# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:16:36 2016

@author: HJohnson

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt

def prime(n):
    sqroot=int(sqrt(n))
    j=2
    while j<=sqroot:
        if n%j==0:
            return False
        j=j+1
    return True
    

num=1
pcnt=0
 
while(1):
    num=num+1
    if prime(num):
        pcnt=pcnt+1
    if pcnt==10001:
        print(pcnt,'th prime is',num)
        break
 