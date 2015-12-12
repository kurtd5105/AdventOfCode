import sys
import re

try:
	with open(sys.argv[1]) as fileInput:
		data = fileInput.read()
except:
	print "File could not be opened."

findRed = re.compile("(:\"red\")")
stack = []
formattedData = ""

i = 0
length = len(data)
while i < length:
	#If there is an object, add its position to the stack
	if data[i] == '{':
		stack.append(i)
	#If there is an object close, check for red
	elif data[i] == '}':
		start = stack.pop()
		#Check for the keyword red within the current object only
		m = findRed.search(data[start:i + 1])
		#If red was not contained check to see if the whole object can be added
		if m is None:
			#If the object isn't nested, we can now add it as it is valid
			if len(stack) == 0:
				formattedData += data[start:i + 1].strip(' ')
		#If red is matched, put whitespace over the object (it may be nested in a valid object)
		else:
			data = data[0:start] + ' ' * len(data[start:i + 1]) + data[i + 1:]
	#If the current data isn't nested in an object then simply add it
	elif len(stack) == 0:
		formattedData += data[i]
	i += 1

#Create an array consisting of all the numbers in the file
m = re.findall("(-?\d+)", data)

#If there were numbers in the file, print the sum of them
if m:
	print sum([int(num) for num in m])
