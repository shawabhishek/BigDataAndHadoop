#!/usr/bin/python

# Alan Shaw
# Assignment 3.2 Next Word bigrams

# Reducer

import fileinput

bigrams = {} 
recommendations = {}

for line in fileinput.input():
	words = line.split()
	if (words[0], words[1]) not in bigrams:
		bigrams[(words[0], words[1])] = 0
	bigrams[(words[0], words[1])] += 1

for bigram in sorted(bigrams, key=bigrams.__getitem__)[::-1]:
	if bigram[0] not in recommendations:
		recommendations[bigram[0]] = set()
	if len(recommendations[bigram[0]]) < 5:
		recommendations[bigram[0]].add(bigram[1])

for key in recommendations:
	if len(recommendations[key]) == 5:
		print(key + '\t' + ', '.join(recommendations[key]))
