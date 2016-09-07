# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 00:25:35 2016

@author: Hunter

A perfect number is a number for which the sum of its proper divisors is
 exactly equal to the number. For example, the sum of the proper divisors
 of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
 than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
 the smallest number that can be written as the sum of two 
 abundant numbers is 24. By mathematical analysis, it can be shown that all
 integers greater than 28123 can be written as the sum of two abundant numbers.
 However, this upper limit cannot be reduced any further by analysis 
 even though it is known that the greatest number that cannot be 
 expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as 
the sum of two abundant numbers.



If nn is odd, it can be written as i+(n−i)i+(n−i) for ii from 11 to (n−1)/2(n−1)/2,
 thus (n−1)/2(n−1)/2 ways. If nn is even, it can be written as i+(n−i)i+(n−i) for ii 
 from 11 to n/2n/2, thus n/2n/2 ways. The case i=n/2i=n/2, i.e. n=(n/2)+(n/2)n=(n/2)+(n/2),
 is the sum of two natural numbers but not the sum of two distinct natural numbers."""


limit = 28123

def isabundant(n): return sum(list(x for x in range(1, int(n/2)+1) if n % x == 0)) > n

def compute():
    abundants = list(x for x in range(1, limit) if isabundant(x) == True)
    sums = 0
    for i in range(12, limit):
        for abundant in abundants:
            if abundant >= i and isabundant(i+abundant) == True: sums += i
    print(sums)

if __name__ == "__main__":
    compute()


