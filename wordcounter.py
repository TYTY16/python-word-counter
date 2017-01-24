#!/usr/bin/python
import sys
import string

wordDictionary = {};

file = open(sys.argv.pop(1), 'r');

for line in file:
	words = line.split();
	for word in words:
		strippedWord = word.translate(string.punctuation);
		if strippedWord in wordDictionary:
			wordDictionary[strippedWord] = wordDictionary[strippedWord] + 1;
		else:
			wordDictionary[strippedWord] = 1;

print(str(wordDictionary));
