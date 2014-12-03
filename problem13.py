#!/usr/bin/python2.7
"""
#=============================================================================#
FILE            : problem13.py

DESCRIPTION     : Project Euler--Problem13 solution/implementation in Python
                  Find the 10-first digits of large sum

#=============================================================================#
"""

input = open ("input13")
print sum([int(line) for line in input])
input.close()
