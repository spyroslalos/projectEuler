#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem05.py

DESCRIPTION     : Project Euler--Problem05 solution/implementation in Python
                  Find smallest num evenly divised by [1, ..., 20]
REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 30 #:#:# CEST 2014

    This program is free software: you can redistribute it and/or modify
    it freely.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
import sys

"""
Check if given number is divisible
by all items of [1, ..., 20]
"""
def div20(num):
    for i in range(1,21):
        if num%i != 0:
            return False
    return True

count = 20
while True:
    if div20(count):
        print count 
        break
    count += 20
