#!/usr/bin/python2.7
"""
#=============================================================================#

FILE            : problem03.py

DESCRIPTION     : Project Euler--Problem3 solution/implementation
		  in Python
		: Find max prime factor of a given number

REQUIREMENTS    : None
BUGS            : Must be somewhere hiding :P.
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 06 23:41:25 CEST 2014

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
import sys
from math import sqrt

# greatest prime factor function
def gpf ():

    # list/all prime factors
    p_facts = []
    n = 600851475143;
    giv = n
    # we start searching prime factors with 2
    d = 2;

    while n>1 :
	while n%d == 0 :
	    p_facts.append (d)
	    n = n/d

	d += 1
	if d > sqrt (n):
	    p_facts.append (n)
	    break

    print "Max prime factor of {0} is {1}".format (giv, max (p_facts) )

if __name__ == "__main__":
    sys.exit(gpf())
