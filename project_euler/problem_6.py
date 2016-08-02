# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:13:02 2016

@author: HJohnson

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten
 natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
 hundred natural numbers and the square of the sum.
"""

square_sum = 5050 ** 2

sumsquares = 0

for i in range(1,101):
    sumsquares += i ** 2

answer = square_sum - sumsquares

print(answer) # 25164150


    
    