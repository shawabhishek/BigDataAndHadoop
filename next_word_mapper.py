#!/usr/bin/python

# Alan Shaw
# Assignment 3.2 Next Word Recommendations

# Mapper

import fileinput
import re

for line in fileinput.input():
	line = re.sub('[^a-z ]', '', line.lower())
	words = line.split()
	for i in range(len(words) - 1): 
		print(words[i] + '\t' + words[i + 1])
