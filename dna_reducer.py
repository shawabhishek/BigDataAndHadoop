#!/usr/bin/python

# Alan Shaw
# Assignment 2.3a Match DNA 2.3b Match DNA forward and backward
# same reducer works for both

# Reducer

import fileinput

relatives = {} 

for line in fileinput.input():
	line_list = line.split()
	if line_list[0] not in relatives:
		relatives[line_list[0]] = set()	
	relatives[line_list[0]].add(line_list[1])

for key in relatives:
	print ', '.join(element for element in sorted(relatives[key]))
