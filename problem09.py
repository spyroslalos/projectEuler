#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem09.py

DESCRIPTION     : Project Euler--Problem09 solution/implementation in Python
                  Pythagorean Triples
REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Dec 01 #:#:# CEST 2014

    This program is free software: you can redistribute it and/or modify
    it freely.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
import sys

class Found(Exception): pass

ul = 1000
try:
    for a in range (1,1000,1):
        for b in range (a+1, 1000,1):
            c=1000-a-b
            if a**2 + b**2 == c**2:
                raise Found
except Found:
    print "Product of abc is %d" % (a*b*c)
