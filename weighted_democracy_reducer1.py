#!/usr/bin/python

# Written by Alan Shaw for the Session 4 Assignment of the Big Data and Hadoop course at http://www.knowbigdata.com for use with Hadoop Streaming.

# Reducer 

# Secondary sort is required in order for this to work
# numerical values before alphabetical values

import fileinput
import re

key = ''
joined_value = 0

for line in fileinput.input():
	line_elements = line.split()
	if key != line_elements[0]: # new key
		joined_value = line_elements[1]
		key = line_elements[0]
		print(line_elements[0] + '\t0')
	else:
		print(line_elements[1] + '\t' + joined_value)
