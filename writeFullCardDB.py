#!/usr/bin/python

import sqlite3
import urllib.request
from bs4 import BeautifulSoup

def main():
	base = "http://yugioh.wikia.com/wiki/"
	file = open("cards_cleaned/cards.txt", "r")
	missingCardsFile = open("missing_cards.txt", "w")

	conn = sqlite3.connect("data/cards_full.db")
	c = conn.cursor()
	c.execute('''CREATE TABLE cards_full (
		cardNumber text, 
		cardName text, 
		cardAttribute text,
		cardType text,
		cardLevel int,
		cardAttack int,
		cardDefense int,
		cardEffect text,
		cardColor text)
		''')

	for line in file:
		try:
			page = urllib.request.urlopen(base+line.split(" ")[0])
			soup = BeautifulSoup(page, "html.parser")
			list_of_a = soup.find_all("a")
			cardColor = soup.find("th")["style"][19:22]

			# FF3 Normal Monster
			# F93 Effect Monster
			# F36 Trap
			# 396 Spell
			# 96C Fusion
			# 66F Ritual Monster
			if cardColor == "FF3":
				start_index = list_of_a.index(soup.find(title="Monster Card"))
				stars = int(list_of_a[list_of_a.index(soup.find(title="Level")) + 1].text)
				c.execute("INSERT INTO cards_full VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
					(line.split(" ")[0],
					line[9:],
					list_of_a[start_index + 2].text,
					list_of_a[start_index + 5].text,
					stars,
					list_of_a[start_index + stars + 10].text,
					list_of_a[start_index + stars + 11].text,
					soup.find(class_="navbox-list").text[1:],
					cardColor))
			elif cardColor == "96C":
				start_index = list_of_a.index(soup.find(title="Monster Card"))
				stars = int(list_of_a[list_of_a.index(soup.find(title="Level")) + 1].text)
				stats_index = list_of_a.index(soup.find(title="ATK"))
				c.execute("INSERT INTO cards_full VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
					(line.split(" ")[0],
					line[9:],
					list_of_a[start_index + 2].text,
					list_of_a[start_index + 5].text + " / " + list_of_a[start_index + 6].text,
					stars,
					list_of_a[stats_index + 2].text,
					list_of_a[stats_index + 3].text,
					soup.find(class_="navbox-list").text[1:],
					cardColor))
			elif cardColor == "F93":
				start_index = list_of_a.index(soup.find(title="Monster Card"))
				stars = int(list_of_a[list_of_a.index(soup.find(title="Level")) + 1].text)
				c.execute("INSERT INTO cards_full VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
					(line.split(" ")[0],
					line[9:],
					list_of_a[start_index + 2].text,
					list_of_a[start_index + 5].text,
					stars,
					list_of_a[start_index + stars + 11].text,
					list_of_a[start_index + stars + 12].text,
					soup.find(class_="navbox-list").text[1:],
					cardColor))
			elif cardColor == "396" or cardColor == "F36":
				start_index = list_of_a.index(soup.find(title="Card type"))
				c.execute("INSERT INTO cards_full VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
					(line.split(" ")[0],
					line[9:],
					list_of_a[start_index + 1].text,
					list_of_a[start_index + 4].text,
					0,
					0,
					0,
					soup.find(class_="navbox-list").text[1:],
					cardColor))
			elif cardColor == "66F":
				start_index = list_of_a.index(soup.find(title="Monster Card"))
				stars = int(list_of_a[list_of_a.index(soup.find(title="Level")) + 1].text)
				stats_index = list_of_a.index(soup.find(title="ATK"))
				c.execute("INSERT INTO cards_full VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
					(line.split(" ")[0],
					line[9:],
					list_of_a[start_index + 2].text,
					list_of_a[start_index + 5].text + " / " + list_of_a[start_index + 6].text,
					stars,
					list_of_a[stats_index + 2].text,
					list_of_a[stats_index + 3].text,
					soup.find(class_="navbox-list").text[1:],
					cardColor))

		except urllib.error.HTTPError:
			missingCardsFile.write(line.split(" ")[0]+"\n")
			pass
		
	
	conn.commit()
	
	'''for row in c.execute("SELECT * FROM effect_cards ORDER BY cardName"):
		print(row)'''

	conn.close()
	file.close()
	missingCardsFile.close()
	
if __name__ == '__main__':
	main()
