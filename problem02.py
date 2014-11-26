#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem02.py

DESCRIPTION     : Project Euler--Problem2 solution/implementation
		  in Python

REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 06 23:04:12 CEST 2014

    This program is free software: you can redistribute it and/or modify
    it under the terms of the Cern.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""


import sys

def fibo ():

    # define start integers
    a = 1
    b = 2 
    flist = []
    flist.append (1)
    flist.append (2)
    c = a + b
    sum = 2

    while True :
	c = a + b
	if c >= 4000000:
	    break
        if c%2 == 0:
	    sum += c
	flist.append(c)
	a = b
	b = c
	print "{0}:{1}".format ( "Current fibonacci: ", c)

    print "Fibonacci list is: {0} and Sum of even numbers is {1}".format(flist, sum)

if __name__ == "__main__":
    fibo ()
    sys.exit

