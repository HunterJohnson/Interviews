# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:27:27 2016

@author: HJohnson

A palindromic number reads the same both ways. The largest palindrome made
 from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

def isPalindrome(n):
    if reverse(n) == n:
        return True
    else:
        return False


largest = 0
i = 100
j = 999

for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        mult = a * b
        if isPalindrome(mult):
            if mult > largest:
                largest = mult


print(largest) #906609



        
    
