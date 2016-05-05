#!/usr/bin/python

# Written by Alan Shaw for the Session 4 Assignment of the Big Data and Hadoop course at http://www.knowbigdata.com for use with Hadoop Streaming

# Find the frequences of letters [a-z] in a text file

# Mapper

# Given a text file fed in from standard input, break each line into words, and each word into letters, then output key = letter, value = 1

import fileinput
import re

for line in fileinput.input():
	line_letters = re.sub('[^a-z]', '', line.lower())
	for i in range(len(line_letters)):
		print(line_letters[i] + '\t' + str(1))
