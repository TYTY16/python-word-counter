#!/usr/bin/python
import sys
import string
import csv

wordDictionary = {};

translator = str.maketrans('', '', string.punctuation);
fieldNames = [ 'word', 'frequency' ];

file = open(sys.argv.pop(1), 'r');

for line in file:
	words = line.split();
	for word in words:
		strippedWord = word.translate(translator).lower();
		if strippedWord in wordDictionary:
			wordDictionary[strippedWord] = wordDictionary[strippedWord] + 1;
		else:
			wordDictionary[strippedWord] = 1;

with open("output.csv",'w') as f:
	w = csv.DictWriter(f, fieldnames=fieldNames);
	w.writeheader();
	for key, value in wordDictionary.items():
		w.writerow({"word":key, "frequency":value});
exit();
