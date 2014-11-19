#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem4.py

DESCRIPTION     : Project Euler--Problem3 solution/implementation
		          in Python
		        :

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


n = 10

# Sum of squares first 10
sqrsum = ( n*(n+1)*(2*n + 1) )/6
print sqrsum

# Square of sums
sumsqr = math.pow(( n*(1+10) )/2, 2)
print sumsqr
