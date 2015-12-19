import sys
import re

try:
	with open(sys.argv[1]) as fileInput:
		replacements = [line.strip() for line in fileInput]
except:
	print "File could not be opened."

string = replacements[-1]
replacements = [line.replace("=> ", "").split() for line in replacements[0:-2]]


def createReplacement(uniqueStrings, string, replacement, start, end):
	replacementString = string[0:start] + replacement + string[end:]
	if replacementString not in uniqueStrings:
		uniqueStrings.append(replacementString)

uniqueStrings = []
for replacement in replacements:
	start = 0
	searchString = "(" + replacement[0] + ").*?"
	r = re.compile(searchString)
	m = r.search(string, start)
	length = len(replacement[0])
	while m:
		start = m.end()
		createReplacement(uniqueStrings, string, replacement[1], m.start(), m.start() + length)
		m = r.search(string, start)

print len(uniqueStrings)
