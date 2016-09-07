# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 14:25:08 2016

@author: Hunter

Find the sum of the digits in the number 100!
"""

import math


def compute():
    result = 0
    for n in str(math.factorial(100)):
        result += int(n)
    print(result)

