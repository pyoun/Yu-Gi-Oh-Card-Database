#!/usr/bin/python

from google import search

def main():
	query = "reversal of graves"
	for url in search(query, tld="co.in", num=10, stop=10):
		print(url)


if __name__ == '__main__':
	main()