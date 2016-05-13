#!/usr/bin/python

# Written by Alan Shaw as an assignment for the Big Data and Hadoop
# course at http://www.knowbigdata.com. For use with Hadoop Streaming.

# Based on the content from a very large text archive, for each word
# prepare a recommmendation list of the top 5 next words.

# Reducer

# Expects bigrams sorted by both words but partitioned only by the first word

# Use this generic option to sort on both fields:
# -D stream.num.map.output.key.fields=2

# Use the KeyFieldBasedPartitioner to partition on only the first field:
# -D mapreduce.partition.keypartitioner.options=-k1
# -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner 

import fileinput
import heapq

# use a heap of tuples
# https://docs.python.org/3.5/library/heapq.html
# "Heap elements can be tuples."

def qualify(recommendations, counter, next_word):
	if len(recommendations) < 5:
		if counter > 0 and len(next_word) > 0:
			heapq.heappush(recommendations, (counter, next_word))
	elif counter > recommendations[0][0]:
		heapq.heappop(recommendations)
		heapq.heappush(recommendations, (counter, next_word))

def output(recommendations, this_word):
	if len(this_word) > 0 and len(recommendations) > 0:
		output_list = list()
		while len(recommendations) > 0:
			output_list.append(heapq.heappop(recommendations)[1])
		print(this_word + ':\t' + ', '.join(output_list))


this_word = ''
recommendations = []
counter = 0
next_word = ''

for line in fileinput.input():
	words = line.split()
	if words[0] != this_word: # new key word
		qualify(recommendations, counter, next_word)
		# before moving on, output this word and its recommendations
		output(recommendations, this_word)
		this_word = words[0]
		next_word = words[1]
		counter = 1
	elif words[1] != next_word: # new next word to count
		# before moving on, decide whether to add the recommendation
		qualify(recommendations, counter, next_word)
		next_word = words[1]
		counter = 1
	else:
		counter += 1
	
qualify(recommendations, counter, next_word)
# output the last word and its recommendations
output(recommendations, this_word)
