#!/usr/bin/python

# Alan Shaw
# Assignment 2.3b  Match DNA forward or backward

# Mapper

import fileinput
import re

for line in fileinput.input():
	# make DNA the key and user the value
	line_elements = line.split()
	if line_elements[1] > line_elements[1][::-1]:
		key = line_elements[1]
	else:
		key = line_elements[1][::-1]
	value = line_elements[0]
	print(key + '\t' + value)
