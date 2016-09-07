# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 17:18:11 2016

@author: Hunter

The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""


def rotate(n):
    rotlist = []
    m = str(n)
    counter = 0
    while counter < len(str(n)):
        m = m[1:] + m[0]
        rotlist.append(int(m))
        counter += 1
    return rotlist

def is_prime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    

from collections import deque
def shifter(num):
 strnum = deque(str(num))
 for i in xrange(len(strnum)):
     yield int(''.join(strnum))
     strnum.rotate()

def compute():
    sum(1 for i in xrange(1000000) if all(is_prime(p) for p in shifter(i))

