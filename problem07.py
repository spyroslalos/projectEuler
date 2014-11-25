#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem07.py

DESCRIPTION     : Project Euler--Problem7 solution/implementation in Python
                  Find the 10001 prime number
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
from myMathAPI import is_prime

nprime = 1
i = 3

while nprime <= 10000:
    if is_prime (i):
        nprime += 1
        print "%d is prime" % (i)
    i += 2
