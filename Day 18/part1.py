import sys

try:
	with open(sys.argv[1]) as fileInput:
		#Create a light array with each line as a sub-array where pound is 1 and . is 0
		lightArray = [[1 if char == '#' else 0 for char in line.strip()] for line in fileInput]
except:
	print "File could not be opened."


def corner(array, left, top, i, j):
	if left:
		if top:
			return (array[i][j + 1] + array[i + 1][j + 1] + array[i + 1][j])
		else:
			return (array[i - 1][j] + array[i - 1][j + 1] + array[i][j + 1])
	else:
		if top:
			return (array[i + 1][j] + array[i + 1][j - 1] + array[i][j - 1])
		else:
			return (array[i][j - 1] + array[i - 1][j - 1] + array[i - 1][j])


def edge(array, vertical, topLeft, i, j):
	#If it is on the left or right side
	if vertical:
		if topLeft:
			return (array[i - 1][j] + array[i - 1][j + 1] + array[i][j + 1]
					+ array[i + 1][j + 1] + array[i + 1][j])
		else:
			return (array[i + 1][j] + array[i + 1][j - 1] + array[i][j - 1]
					+ array[i - 1][j - 1] + array[i - 1][j])
	#If it is on the top or bottom side
	else:
		if topLeft:
			return (array[i][j + 1] + array[i + 1][j + 1] + array[i + 1][j]
					+ array[i + 1][j - 1] + array[i][j - 1])
		else:
			return (array[i][j - 1] + array[i - 1][j - 1] + array[i - 1][j]
					+ array[i - 1][j + 1] + array[i][j + 1])


def middle(array, i, j):
	return (array[i - 1][j] + array[i - 1][j + 1] + array[i][j + 1]
			+ array[i + 1][j + 1] + array[i + 1][j] + array[i + 1][j - 1]
			+ array[i][j - 1] + array[i - 1][j - 1])


def animate(light, adjacentOn):
	#Return the state of the light based on the game rules
	if light:
		if adjacentOn == 2 or adjacentOn == 3:
			return 1
		else:
			return 0
	else:
		if adjacentOn == 3:
			return 1
		else:
			return 0


prevArray = [list(array) for array in lightArray]
for step in xrange(100):
	for i in xrange(100):
		for j in xrange(100):
			adjacentOn = 0
			#If in the first row
			if i == 0:
				#If in the left corner
				if j == 0:
					adjacentOn = corner(prevArray, 1, 1, i, j)
					lightArray[i][j] = animate(prevArray[i][j], adjacentOn)
				#If in the right corner
				elif j == 99:
					adjacentOn = corner(prevArray, 0, 1, i, j)
					lightArray[i][j] = animate(prevArray[i][j], adjacentOn)
				#If on the top edge
				else:
					adjacentOn = edge(prevArray, 0, 1, i, j)
					lightArray[i][j] = animate(prevArray[i][j], adjacentOn)

			#If in the last row
			elif i == 99:
				#If in the left corner
				if j == 0:
					adjacentOn = corner(prevArray, 1, 0, i, j)
					lightArray[i][j] = animate(prevArray[i][j], adjacentOn)
				#If in the right corner
				elif j == 99:
					adjacentOn = corner(prevArray, 0, 0, i, j)
					lightArray[i][j] = animate(prevArray[i][j], adjacentOn)
				#If on the bottom edge
				else:
					adjacentOn = edge(prevArray, 0, 0, i, j)
					lightArray[i][j] = animate(prevArray[i][j], adjacentOn)

			#If in any row between 0 and the end
			else:
				#If on the left edge
				if j == 0:
					adjacentOn = edge(prevArray, 1, 1, i, j)
					lightArray[i][j] = animate(prevArray[i][j], adjacentOn)
				#If on the right edge
				elif j == 99:
					adjacentOn = edge(prevArray, 1, 0, i, j)
					lightArray[i][j] = animate(prevArray[i][j], adjacentOn)
				#If surrounded by other lights
				else:
					adjacentOn = middle(prevArray, i, j)
					lightArray[i][j] = animate(prevArray[i][j], adjacentOn)

	prevArray = [list(array) for array in lightArray]


total = 0
for line in lightArray:
	total += sum(line)

print total
