#!/usr/bin/python

import sqlite3

def main():
	file = open("cards_cleaned/cards.txt", "r")

	conn = sqlite3.connect("data/cards.db")
	c = conn.cursor()
	c.execute('''CREATE TABLE cards (cardNumber text, cardName text)''')

	for line in file:
		c.execute("INSERT INTO cards VALUES (?, ?)", 
			(line.split(" ")[0], line[9:]))

	conn.commit()
	
	for row in c.execute("SELECT * FROM cards ORDER BY cardName"):
		print(row)

	conn.close()
	
if __name__ == '__main__':
	main()
