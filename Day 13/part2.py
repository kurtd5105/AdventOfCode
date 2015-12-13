import sys
import itertools

try:
	with open(sys.argv[1]) as fileInput:
		happinessInput = [line.strip() for line in fileInput]
except:
	print "File could not be opened."

happiness = []
people = set()

for line in happinessInput:
	#Remove the useless words in each sentence, and replace lose with a negative sign
	line = line.replace("lose ", " -").replace("gain", "").replace(" would ", "")
	line = line.replace("happiness units by sitting next to ", "").replace(".", "")

	#Split up the line into the 3 remaining items: Person, happiness, Person 2
	line = line.split(" ")

	#Add the adjacent people to a set
	people.add(line[0])
	people.add(line[2])

	line[1] = int(line[1])

	#Add the parsed data to the happiness list
	happiness.append(list(line))

#happinessSets[i] contains a dictionary with the names of the other people as the keyword
#and the happiness of person[i] sitting next to the other person as the value
happinessSets = [{}]

#peopleSets is a dictionary with the every person as a keyword and their index in the
#happinessSets as the value
peopleSets = {}
person = happiness[0][0]
i = 0
peopleSets[person] = 0

for group in happiness:
	#If the person is different
	if group[0] != person:
		#Increment i, add the person to the peopleSet
		i += 1
		peopleSets[group[0]] = i
		#Create a new dictionary for that person in happinessSets
		happinessSets.append({})
		person = group[0]

	#Add the other person as a keyword to the current person's dict and the happiness value
	happinessSets[i][group[2]] = group[1]

#Add myself to the group with a happiness value of 0 for everyone
happinessSets.append({})
for person in peopleSets:
	people.add("Myself")
	people.add(person)
	happinessSets[-1][person] = 0
	happinessSets[peopleSets[person]]["Myself"] = 0
peopleSets["Myself"] = i + 1


maxHappiness = 0
maxPeople = None

length = len(peopleSets)
#Check the happiness of every permutation
for items in itertools.permutations(people):
	temp = 0
	#For every group of people in a given permutation
	for i in range(length - 1):
		#Add the happiness value of Person 1 next to Person 2 and vice-versa
		temp += happinessSets[peopleSets[items[i]]][items[i + 1]]
		temp += happinessSets[peopleSets[items[i + 1]]][items[i]]
	#Add the values for the first and last person in the permutation since the table is round
	temp += happinessSets[peopleSets[items[-1]]][items[0]]
	temp += happinessSets[peopleSets[items[0]]][items[-1]]

	if temp > maxHappiness:
		maxHappiness = temp
		maxPeople = items

print maxPeople
print maxHappiness
