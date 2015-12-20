import sys
import re

try:
	with open(sys.argv[1]) as fileInput:
		replacements = [line.strip() for line in fileInput]
except:
	print "File could not be opened."

#The last string in the file is the molecule
string = replacements[-1]

#The replacements are the rest of the file minus the last two lines
replacements = [line.replace("=> ", "").split() for line in replacements[0:-2]]


def createReplacement(uniqueStrings, string, replacement, start, end):
	#Splice the replacement in
	replacementString = string[0:start] + replacement + string[end:]

	#Add it to the list if it isn't already there
	if replacementString not in uniqueStrings:
		uniqueStrings.append(replacementString)

uniqueStrings = []
#Create a list of unique strings from every possible replacement
for replacement in replacements:
	start = 0
	#Create the regex string
	searchString = "(" + replacement[0] + ").*?"
	r = re.compile(searchString)

	#Find every match for replacement
	m = r.search(string, start)
	length = len(replacement[0])
	while m:
		start = m.end()
		#Create the replacement for the match
		createReplacement(uniqueStrings, string, replacement[1], m.start(), m.start() + length)
		m = r.search(string, start)

print len(uniqueStrings)
