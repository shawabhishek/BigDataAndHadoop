#!/usr/bin/python

# Written by Alan Shaw for the Session 4 Assignment of the Big Data and Hadoop course at http://www.knowbigdata.com for use with Hadoop Streaming

# Find the frequences of letters [a-z] in a text file

# Reducer

# Given sorted input of key = letter, value = 1, sum per letter and output letter and its sum

# I originally used a Python dictionary, but that doesn't take advantage (performance-wise) of the sort that Hadoop has already done.

import fileinput

frequencies = list()
letter = ''

for line in fileinput.input():
	if line[0] != letter:
		letter = line[0]
		frequencies.append([letter, 1])
	else:
		frequencies[-1][1] += 1

for i in range(len(frequencies)):
	print(frequencies[i][0] + '\t' + str(frequencies[i][1]))
