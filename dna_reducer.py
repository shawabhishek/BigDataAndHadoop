#!/usr/bin/python

# Written by Alan Shaw for the Session 4 Assignment of the Big Data and Hadoop course at http://www.knowbigdata.com for use with Hadoop Streaming.

# A file contains the DNA sequence of people. Find all the people who have the same DNA. 
# same reducer works for both

# Reducer

# Given sorted input of a DNA key plus a user as value, group the users for a given key together and output this set before moving on to the next key.

import fileinput

relatives = set()
key = ''

for line in fileinput.input():
	line_list = line.split()
	if line_list[0] != key: # new key
		if len(relatives) > 0:
			print ', '.join(element for element in relatives)
		key = line_list[0]
		relatives = set()
	relatives.add(line_list[1])

# the final set won't have a new key trigger
if len(relatives) > 0:
	print ', '.join(element for element in relatives)
