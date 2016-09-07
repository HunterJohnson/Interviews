# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 23:16:52 2016

@author: Hunter

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import math


def compute():
    result = 0
    for n in str(2**1000):
        result += int(n)
    print(result)

if __name__ == "__main__":
    compute()


