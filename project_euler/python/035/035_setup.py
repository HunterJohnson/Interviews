# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 17:41:10 2016

@author: Hunter
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("thirtyfive.pyx")
)