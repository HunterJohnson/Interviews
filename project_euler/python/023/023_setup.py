# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 01:14:12 2016

@author: Hunter
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("twentythree.pyx")
)