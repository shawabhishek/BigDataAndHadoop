#!/usr/bin/python

# Written by Alan Shaw for the Session 4 Assignment of the Big Data and Hadoop course at http://www.knowbigdata.com for use with Hadoop Streaming.

# Find all the words that are anagrams of each other in a huge text

# Reducer

# Given sorted input of key = alphabetically sorted string of a word, value = the unsorted word, group all of the unique words for each key and output this set (as long as there is more than one) before going on to the next key.

# I originally used a Python dictionary, but that doesn't take advantage (performance-wise) of the sort that has already been done.

import fileinput

anagrams = set()
key = ''

for line in fileinput.input():
	line_list = line.split()
	if line_list[0] != key: # new key
		if len(anagrams) > 1:
			print ', '.join(element for element in anagrams)
		key = line_list[0]
		anagrams = set()
	anagrams.add(line_list[1])

# the final set won't have a new key trigger
if len(anagrams) > 1:
	print ', '.join(element for element in anagrams)
