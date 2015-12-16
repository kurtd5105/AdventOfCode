import sys
import re

try:
	with open(sys.argv[1]) as fileInput:
		aunts = [line.strip().replace(":", "").replace(",", "").replace("Sue ", "").split(" ")
					for line in fileInput]
except:
	print "File could not be opened."

auntData = []
for aunt in aunts:
	#Parse the aunt info so that every string that is an int is stored as an int
	auntInfo = [int(data) if re.match("(-?\d+)", data) else data
				for data in aunt[1:]]
	auntDict = {}
	#Construct a dictionary with the compound as the key and their values
	for i in range(len(auntInfo)):
		#If it's a string then it's a key
		if isinstance(auntInfo[i], str):
			#The next element will be a value
			auntDict[auntInfo[i]] = auntInfo[i + 1]

	auntData.append(auntDict)

include = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "goldfish": 5,
			"trees": 3, "cars": 2, "perfumes": 1, "akitas": 0, "vizslas": 0}

result = 0
length = len(auntData)
requiredMatches = len(include)
matches = []

#Check for aunts that match the compounds given
for aunt in range(0, length):
	match = 0
	for compound in auntData[aunt]:
		if compound in include:
			#If the compound has the wrong value then the aunt cant be ruled out entirely
			if include[compound] != auntData[aunt][compound]:
				match = -1
				break
			else:
				match += 1

	#If the aunt wasn't ruled out then append the match count and aunt number
	if match != -1:
		matches.append((match, aunt))

	#If a full match is found then set the result and stop searching
	if match == requiredMatches:
		result = aunt + 1
		break

#If no complete match was found
if result == 0:
	highest = 0
	for group in matches:
		if group[0] > highest:
			highest = group[0]
			result = group[1]
	result += 1

print result
