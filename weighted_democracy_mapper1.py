#!/usr/bin/python

# Written by Alan Shaw for the Session 4 Assignment of the Big Data and Hadoop course at http://www.knowbigdata.com for use with Hadoop Streaming.

# Inputs from two lists:
# List1 = Voter, Votee
# List2 = Person, Worth

# Mapper

# Two outputs per record

import fileinput
import numpy
import re

for line in fileinput.input():
	line_elements = line.split()
	print(line_elements[0] + '\t' + line_elements[1])
