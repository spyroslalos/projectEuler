#!/usr/bin/python2.7
"""
#=============================================================================#
FILE            : problem11.py

DESCRIPTION     : Project Euler--Problem11 solution/implementation in Python
                  Max product on Grid

REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Dec 6 #:#:# CEST 2014

    This program is free software: you can redistribute it and/or modify
    it freely.
#=============================================================================#
"""

input = open ("input11")
arr2d = []
for line in input:
    tmp = line.rstrip().split(" ")
    arr2d.append(tmp)
    print arr2d
