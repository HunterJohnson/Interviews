# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:52:48 2016
@author: HJohnson

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt

def isPrime(n):
    sqroot=int(sqrt(n))
    j=2
    while j<=sqroot:
        if n%j==0:
            return False
        j=j+1
    return True

answer = 0

for i in range(2,2000000):
    if isPrime(i):
        answer += i

print(answer) # 142913828922



    
    