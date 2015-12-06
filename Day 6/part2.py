import sys

#Set up a 1000 by 1000 array of lights initialized to False
row = [0 for x in xrange(1000)]
lights = [list(row) for x in xrange(1000)]

instructions = []
try:
	with open(sys.argv[1]) as fileInput:
		#Take each line of input, remove "through" and "turn" and split it at the spaces
		instructions = [line.strip().replace("through", "").replace("turn", "").split()
						for line in fileInput]
except:
	print "File could not be opened."

#Apply each instruction to the light array
for instruction in instructions:
	#Convert the first set of CSV to the start and the second to the end 
	start = [int(x) for x in instruction[1].split(',')]
	#Add 1 since an inclusive range is needed and range() has an exclusive upper bound
	end = [int(x) + 1 for x in instruction[2].split(',')]

	#Change the values of the light array according to the instruction within
	if instruction[0] == "off":
		for i in range(start[0], end[0]):
			for j in range(start[1], end[1]):
				if lights[i][j] >= 1:
					lights[i][j] -= 1
	elif instruction[0] == "on":
		for i in range(start[0], end[0]):
			for j in range(start[1], end[1]):
				lights[i][j] += 1
	elif instruction[0] == "toggle":
		for i in range(start[0], end[0]):
			for j in range(start[1], end[1]):
				lights[i][j] += 2

total = 0
for i in xrange(1000):
	total += sum(lights[i])
print total