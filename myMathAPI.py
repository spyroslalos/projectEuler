#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : myMathAPI.py

DESCRIPTION     : My personal math module in python

REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 24 #:#:# CEST 2014

    This program is free software: you can redistribute it and/or modify
    it under the terms of the Cern.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
import math

def is_prime (n):
    for i in range (2,int(math.sqrt(n)+1)):
        if ( n%i ) == 0:
            return False
    return True

def my_palindrome (num):
    return str(num) == str(num)[::-1]

def dumb_sum_digits (num):
    return sum( [int(n) for n in str(num)] )
