# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:35:23 2016

@author: HJohnson

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for i in range(1,700):
    for j in range(1,700):
        for k in range(1,700):
            if i + j + k == 1000:
                if i**2 + j**2 == k**2:
                    print(i * j * k)   # 31875000
                    
