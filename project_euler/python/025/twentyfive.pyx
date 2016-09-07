# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 01:32:18 2016

@author: Hunter

025 


The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def compute():
    maxi = 0
    maxlen = 0
    for i in range(1,150):
        leni = len(str(fibonacci(i)))
        if leni > maxlen:
            maxlen = leni
            maxi = i
    print(maxi, maxlen)
    


        
