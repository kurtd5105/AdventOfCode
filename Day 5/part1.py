import sys
import re

strings = []
try:
	with open(sys.argv[1]) as fileInput:
		#Put every line of the input into a list of strings
		strings = [line.strip() for line in fileInput]
except:
	print "File could not be opened."

total = 0
for string in strings:
	#If it has at least 3 vowels
	if re.search("((a|e|i|o|u).*){3,}", string):
		#If it has at least 1 set of repeating characters
		if re.search("((\w)\\2)", string):
			#If it doesnt contain ab, cd, pq, xy it is a nice string
			if not re.search("(ab|cd|pq|xy)", string):
				total += 1

print total