#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem10.py

DESCRIPTION     : Project Euler--Problem10 solution/implementation in Python
                  Sum of prime numbers under 2000000

REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 27 #:#:# CEST 2014

    This program is free software: you can redistribute it and/or modify
    it freely.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
import math
from myMathAPI import is_prime

sum = 2
i = 3

# dumb solution -> needs improvement
while i < (2000000):
    if is_prime(i):
        sum = sum + i
        print "%d is prime" % (i)
    i += 2

print sum
