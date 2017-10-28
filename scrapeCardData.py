#!/usr/bin/python

import urllib.request
from bs4 import BeautifulSoup


def main():
	base = "http://yugioh.wikia.com/wiki/"
	urls = ["Gagagigo", "Exchange_of_the_Spirit", "Dark_Magician_Girl", 
	"Fissure", "Blue-Eyes_Ultimate_Dragon"]

	for link in urls:
		page = urllib.request.urlopen(base+link)
		soup = BeautifulSoup(page, "html.parser")
		style = soup.find("th")["style"]
		# print hex color representing type of card
		print(style[19:22])
		# FF3 Normal Monster
		# F36 Trap
		# F93 Effect Monster
		# 396 Spell
		# 96C



if __name__ == "__main__":
	main()