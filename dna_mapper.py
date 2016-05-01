#!/usr/bin/python

# Alan Shaw
# Assignment 2.3a  Match DNA

# Mapper

import fileinput
import re

for line in fileinput.input():
	# make DNA the key and user the value
	line_elements = line.split()
	key = line_elements[1]
	value = line_elements[0]
	print(key + '\t' + value)
