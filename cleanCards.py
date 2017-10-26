#!/usr/bin/python

def main():
	cards1 = "cards_raw/cards1.txt"
	cards2 = "cards_raw/cards2.txt"
	cards3 = "cards_raw/cards3.txt"
	file1 = open(cards1, "r")
	file2 = open(cards2, "r")
	file3 = open(cards3, "r")

	cardDict = {}
	# to confirm that no replicates were added
	cardSet = set()
	
	for line in file1:
		cardDict[line.split(" ")[0]] = line[9:]
		cardSet.add(line.split(" ")[0])

	for line in file2:
		cardNumber = line.split(" ")[0]
		cardSet.add(cardNumber)
		if cardNumber not in cardDict:
			cardDict[cardNumber] = line[9:]

	for line in file3:
		cardNumber = line.split(" ")[0]
		cardSet.add(cardNumber)
		if cardNumber not in cardDict:
			cardDict[cardNumber] = line[9:]

	# to print key,value cardNumber,cardName
	for key in cardDict:
		print(key + ": " + cardDict[key])
	if len(cardSet) == len(cardDict):
		print("Number of cards: " + str(len(cardSet)))

	file = open("cards_cleaned/cards.txt", "w")
	for key, value in cardDict.items():
		file.write(key + " " + value)

if __name__ == '__main__':
	main()
