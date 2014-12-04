#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem20.py

DESCRIPTION     : Project Euler--Problem20 solution/implementation in Python
                  Factorial and sum of digits
REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Dec 4 #:#:# CEST 2014

    This program is free software: you can redistribute it and/or modify
    it freely.

#=============================================================================#
"""
from myMathAPI import dumb_sum_digits

# Calculate factorial function
def factorial (num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

# Print sum of digits 
print dumb_sum_digits(factorial(100))
