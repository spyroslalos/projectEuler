#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem25.py

DESCRIPTION     : Project Euler--Problem25 solution/implementation
		          in Python

REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 28 #:#:# CEST 2014

    This program is free software: you can redistribute it and/or modify
    it under the terms of the Cern.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
import math
import sys


# define start fibonacci
a = 1
b = 2 
# 1,1,2 preceding fibo numbers
term = 3
flist = []
flist.append (1)
flist.append (2)
c = a + b
sum = 2

while True :
    c = a + b
    term += 1
    if (int(math.log10(c))+1) == 1000:
        break
    a = b
    b = c

print "Term for fibo number with 1000 digits = %d" % (term)
