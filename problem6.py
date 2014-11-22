#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem6.py

DESCRIPTION     : Project Euler--Problem6 solution/implementation in Python
		: Find square of sums and sum of squares of a sequence of numbers

REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 19 #:#:# CEST 2014

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
import sys
import math


n = 100

# Sum of squares first 10
sqrsum = ( n*(n+1)*(2*n + 1) )/6
print sqrsum

# Square of sums
sumsqr = math.pow(( n*(1+100) )/2, 2)
print sumsqr

print "{0} is : {1}".format(sumsqr, sqrsum)

print  "Difference is : {0}".format(sumsqr - sqrsum)

