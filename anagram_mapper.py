#!/usr/bin/python

# Alan Shaw
# Assignment 2.2 Find anagrams

# Mapper

import fileinput
import re

for line in fileinput.input():
	line = re.sub('[^a-z ]', '', line.lower())
	for word in line.split():
		key = ''.join(sorted(list(word)))
		print(key + '\t' + word)
