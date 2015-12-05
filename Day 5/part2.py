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
	#If a string has a set of repeating characters twice
	if re.search("(((\w){2}).*?\\2)", string):
		#If a string has a set of the same characters with different one in the middle
		if re.search("(((\w)).\\2)", string):
			total += 1

print total