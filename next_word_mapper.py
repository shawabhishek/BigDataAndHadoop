#!/usr/bin/python

# Written by Alan Shaw as an assignment for the Big Data and Hadoop
# course at http://www.knowbigdata.com. For use with Hadoop Streaming.

# Based on the content from a very large text archive, for each word
# prepare a recommmendation list of the top 5 next words.

# Mapper

# Output all bigrams (consecutive two word combinations),
# including those that cross over lines

import fileinput
import re

next_word = ''

for line in fileinput.input():
	# strip out everything except letters, spaces, and punctuation
	line = re.sub('[^a-z 0-9]', '', line.lower())
	words = line.split()
	# first output bigrams that cross lines
	this_word = next_word
	if len(words) > 0:
		next_word = words[0]
	else:
		next_word = ''
	if len(this_word) > 0 and len(next_word) > 0:
		print(this_word + '\t' + next_word)
	# now iterate through the rest of the line
	for i in range(len(words) - 1): 
		this_word = words[i]
		next_word = words[i + 1]
		if len(this_word) > 0 and len(next_word) > 0:
			print(this_word + '\t' + next_word)
