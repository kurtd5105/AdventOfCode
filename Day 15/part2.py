import sys
import re
import operator

try:
	with open(sys.argv[1]) as fileInput:
		cookieData = [line.strip().replace(":", "").replace(",", "").split(" ")
						for line in fileInput]
except:
	print "File could not be opened."

ingredients = []
properties = []

ingredientProperties = {}
for ingredient in cookieData:
	ingredients.append(ingredient[0])
	#Parse the ingredient info so that every string that is an int is stored as an int
	ingredientInfo = [int(data) if re.match("(-?\d+)", data) else data
						for data in ingredient[1:]]
	ingredientDict = {}
	#Construct a dictionary with the ingredient properties as the key and their values
	for i in range(len(ingredientInfo)):
		#If it's a string then it's a key
		if isinstance(ingredientInfo[i], str):
			#Add unique properties that aren't calories
			if ingredientInfo[i] != "calories" and ingredientInfo[i] not in properties:
				properties.append(ingredientInfo[i])
			#The next element will be a value
			ingredientDict[ingredientInfo[i]] = ingredientInfo[i + 1]

	#Add the constructed dictionary as the value for that ingredient
	ingredientProperties[ingredient[0]] = ingredientDict

count = len(ingredients)
currMax = 0

#Iterate over every possible grouping of ingredients
for i in xrange(101):
	for j in xrange(101 - i):
		for k in xrange(101 - i - j):
			l = 100 - i - j - k
			items = [i, j, k, l]
			#Make sure that the total amount of ingredients isn't more than 100
			if sum(items) == 100:
				skip = False
				ingredientCount = {}
				propertyScore = {}

				#Setup the ingredient count and propertyScore dictionaries to have 0 values
				for ingredient in ingredients:
					ingredientCount[ingredient] = 0
				for prop in properties:
					propertyScore[prop] = 0

				a = 0
				#Set the ingredient count for every ingredient to its count
				for ingredient in ingredients:
					ingredientCount[ingredient] = items[a]
					a += 1

				#Calculate the amount of calories for this cookie
				calories = 0
				for ing in ingredients:
					calories += ingredientProperties[ing]["calories"] * ingredientCount[ing]

				if calories == 500:
					#Calculate the score for every property in every ingredient
					for ing in ingredients:
						for prop in properties:
							propertyScore[prop] += ingredientProperties[ing][prop] * ingredientCount[ing]

					#Check if any score is below 0, if so skip scoring it since it is worth 0 score
					for prop in propertyScore:
						if propertyScore[prop] < 0:
							skip = True
							break

					if not skip:
						#Multiply all the values together
						result = reduce(operator.mul, [val for key, val in propertyScore.iteritems()])
						if result > currMax:
							currMax = result

print currMax
