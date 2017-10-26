#!/usr/bin/python

import re

def main():
	cards = "cards.txt"
	file = open(cards, "r")

	consecdots = re.compile(r'\.{3,}')

	for line in file:
		line = consecdots.sub('', line)
		print(line)
	
if __name__ == '__main__':
	main()
