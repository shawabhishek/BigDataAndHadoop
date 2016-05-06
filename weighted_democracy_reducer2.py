#!/usr/bin/python

# Written by Alan Shaw for the Session 4 Assignment of the Big Data and Hadoop course at http://www.knowbigdata.com for use with Hadoop Streaming.

# Input from the first mapreduce job:
#	A	0
#	B	0
#	C	0
#	C	1
#	C	5
#	F	11

# Mapper

# Aggregate by key

import fileinput
import re

key = ''

for line in fileinput.input():
	line_elements = line.split()
	if len(line_elements) > 1:
		if key != line_elements[0]:
			if key != '':
				print(key + '\t' + str(vote_count))
			vote_count = int(line_elements[1])
			key = line_elements[0]
		else:
			vote_count += int(line_elements[1])
print(key + '\t' + str(vote_count))
