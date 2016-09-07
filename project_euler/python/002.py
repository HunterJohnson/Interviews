# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:01:09 2016

@author: HJohnson

Each new term in the Fibonacci sequence is generated by adding the previous
 twoterms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
 exceed four million, find the sum of the even-valued terms.
"""

def fibonacci(n):
    if n <= 2:
        return n
    else:
       return fibonacci(n-2) + fibonacci(n-1)
        
print(fibonacci(32)) # last fib < 4M

answer = 0

for i in range(1,33):
    n = fibonacci(i)
    if n % 2 == 0:
        answer += n

print(answer) 



        




    
    
