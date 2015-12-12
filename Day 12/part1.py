import sys
import re

try:
	with open(sys.argv[1]) as fileInput:
		data = fileInput.read()
except:
	print "File could not be opened."

#Create an array consisting of all the numbers in the file
m = re.findall("(-?\d+)", data)

#If there were numbers in the file, print the sum of them
if m:
	print sum([int(num) for num in m])
