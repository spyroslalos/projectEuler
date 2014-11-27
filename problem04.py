#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem04.py

DESCRIPTION     : Project Euler--Problem04 solution/implementation in Python
                  Find the largest possible palindronme
REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 27 #:#:# CEST 2014

    This program is free software: you can redistribute it and/or modify
    it under the terms of the Cern.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
from myMathAPI import my_palindrome
viable_palin = []

for i in range( 999, -1, -1 ):
    for j in range( 999, -1, -1 ):
        if my_palindrome( i*j ):
            print i, j
            viable_palin.append( i*j )

print viable_palin  
print max( viable_palin )
