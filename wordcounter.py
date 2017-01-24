#!/usr/bin/python
import sys
import string

wordDictionary = {};

translator = str.maketrans('', '', string.punctuation);

file = open(sys.argv.pop(1), 'r');

for line in file:
	words = line.split();
	for word in words:
		strippedWord = word.translate(translator).lower();
		if strippedWord in wordDictionary:
			wordDictionary[strippedWord] = wordDictionary[strippedWord] + 1;
		else:
			wordDictionary[strippedWord] = 1;

print(str(wordDictionary));
