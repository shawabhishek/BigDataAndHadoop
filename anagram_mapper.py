#!/usr/bin/python

# Written by Alan Shaw for the Session 4 Assignment of the Big Data and Hadoop course at http://www.knowbigdata.com for use with Hadoop Streaming.

# Find all the words that are anagrams of each other in a huge text

# Mapper

# Split the input text into individual words, ignoring punctuation. Sort the letters of the word in alphabetical order and output this sorted string as the key, with the value being the original (unsorted) word.

import fileinput
import re

for line in fileinput.input():
	line = re.sub('[^a-z ]', '', line.lower())
	for word in line.split():
		key = ''.join(sorted(list(word)))
		print(key + '\t' + word)
