#!/usr/bin/python

import urllib.request
from bs4 import BeautifulSoup


def main():
	base = "http://yugioh.wikia.com/wiki/"
	urls = ["Gagagigo", "Exchange_of_the_Spirit", "Dark_Magician_Girl", 
	"Fissure", "Blue-Eyes_Ultimate_Dragon"]
	
	gagagigo = []
	dmgg = []
	exchange = []
	fissure = []
	beud = []

	for link in urls:
		page = urllib.request.urlopen(base+link)
		soup = BeautifulSoup(page, "html.parser")
		style = soup.find("th")["style"]
		# print hex color representing type of card
		# print(style[19:22])
		# FF3 Normal Monster
		# F93 Effect Monster
		# F36 Trap
		# 396 Spell
		# 96C Fusion
		
		cardType = style[19:22] 
		
		if cardType == "FF3":
			list_of_a = soup.find_all("a")
			start_index = list_of_a.index(soup.find(title="Monster Card"))
			gagagigo.append(list_of_a[start_index + 2].text)
			gagagigo.append(list_of_a[start_index + 5].text)
			stars = list_of_a[start_index + 7].text
			gagagigo.append(stars)
			gagagigo.append(list_of_a[start_index + int(stars) + 10].text)
			gagagigo.append(list_of_a[start_index + int(stars) + 11].text)
		elif cardType == "F93":
			list_of_a = soup.find_all("a")
			start_index = list_of_a.index(soup.find(title="Monster Card"))
			dmgg.append(list_of_a[start_index + 2].text)
			dmgg.append(list_of_a[start_index + 5].text)
			stars = list_of_a[start_index + 8].text
			dmgg.append(stars)
			dmgg.append(list_of_a[start_index + int(stars) + 11].text)
			dmgg.append(list_of_a[start_index + int(stars) + 12].text)
		elif cardType == "96C":
			list_of_a = soup.find_all("a")
			start_index = list_of_a.index(soup.find(title="Monster Card"))
			beud.append(list_of_a[start_index + 2].text)
			beud.append(list_of_a[start_index + 5].text)
			stars = list_of_a[start_index + 8].text
			beud.append(stars)
			beud.append(list_of_a[start_index + int(stars) + 11].text)
			beud.append(list_of_a[start_index + int(stars) + 12].text)
		elif cardType == "396":
			fissure.append("SPELL")
			for i in range(4):
				fissure.append("")
		elif cardType == "F36":
			exchange.append("TRAP")
			for i in range(4):
				exchange.append("")


	print(gagagigo)
	print(dmgg)
	print(exchange)
	print(fissure)
	print(beud)



if __name__ == "__main__":
	main()