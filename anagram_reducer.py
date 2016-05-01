#!/usr/bin/python

# Alan Shaw
# Assignment 2.2 Find anagrams

# Reducer

import fileinput

candidates = {} 

for line in fileinput.input():
	line_list = line.split()
	if line_list[0] not in candidates:
		candidates[line_list[0]] = set()	
	candidates[line_list[0]].add(line_list[1])

for key in candidates:
	if len(candidates[key]) > 1:
		print ', '.join(element for element in candidates[key])
