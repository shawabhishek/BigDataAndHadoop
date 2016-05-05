#!/usr/bin/python

# Written by Alan Shaw for the Session 4 Assignment of the Big Data and Hadoop course at http://www.knowbigdata.com for use with Hadoop Streaming.

# A file contains the DNA sequence of people. Find all the people who have the same DNA. 

# Mapper

# Output the DNA string as the key and the user as the value

import fileinput
import re

for line in fileinput.input():
	# make DNA the key and user the value
	line_elements = line.split()
	key = line_elements[1]
	value = line_elements[0]
	print(key + '\t' + value)
