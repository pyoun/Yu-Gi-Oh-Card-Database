#!/usr/bin/python

from google import search
import sqlite3

def grabURLs():
	# connect to cards database
	conn = sqlite3.connect("data/cards.db")
	c = conn.cursor()

	cardNameList = []
	# make a list of card names
	for row in c.execute("SELECT cardName FROM cards"):
		cardNameList.append(row[0])
	#for card in cardNameList: print(card)

	for card in cardNameList:
		lst = []
		for url in search("yugioh" + card, tld="co.in", num=5, stop=5):
			if "yugioh.wikia.com/wiki/" in url:
				lst.append(url)
		#usually the link we need for the correct card
		print(lst[0])

		
	'''
	query = "a team trap removal"
	lst = []
	for url in search(query, tld="co.in", num=10, stop=10):
		lst.append(url)

	#grab only the wiki links
	wikilist = []
	for url in lst:
		if "yugioh.wikia.com/wiki/" in url:
			wikilist.append(url)

	for item in wikilist:
		print(item)
	'''



if __name__ == '__main__':
	grabURLs()