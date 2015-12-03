import sys

def isValidSymbol(char):
	return char == '<' or char == '>' or char == '^' or char == 'v'

def symbolToMove(char):
	#Convert the movement symbols to a movement in the x, y direction
	if char == '^':
		return [0, 1]
	elif char == '>':
		return [1, 0]
	elif char == 'v':
		return [0, -1]
	return [-1, 0]

def insertInOrder(houses, pos):
	#Inserts unique houses visited in order
	#
	#Could be sped up with a more efficient insertion technique
	#Houses list could be in form houses[pos[0]] is a list of y positions, or have houses[i]
	#contain the first x and the rest be y positions
	i = 0
	j = 0
	length = len(houses)
	while pos[0] > houses[i][0][0]:
		i += 1
		if i >= length:
			break
	if i < length:
		#If there are other houses with index i visited
		if pos[0] == houses[i][0][0]:
			length = len(houses[i])
			while pos[1] > houses[i][j][1]:
				j += 1
				if j >= length:
					break
			#If the position has to be inserted
			if j < length:
				#If the position is unique then insert it
				if pos[1] != houses[i][j][1]:
					houses[i].insert(j, list(pos))
			else:
				houses[i].append(list(pos))
		else:
			houses.insert(i, [list(pos)])
	else:
		houses.append([list(pos)])
	return houses


try:
	with open(sys.argv[1]) as fileInput:
		#Create a list of x, y increments from the directional input
		moves = [symbolToMove(char) for char in fileInput.read() if isValidSymbol(char)]
		# 			x, y
		santaPos = [0, 0]
		roboPos = [0, 0]
		#Unique houses visited
		houses = [[[0, 0]]]
		i = 0
		for move in moves:
			#If i is even move Santa, otherwise move Robo-Santa
			if i % 2 == 0:
				santaPos[0] += move[0]
				santaPos[1] += move[1]
				houses = insertInOrder(houses, santaPos)
			else:
				roboPos[0] += move[0]
				roboPos[1] += move[1]
				houses = insertInOrder(houses, roboPos)
			i += 1

		total = 0
		#The amount of houses visited are the length of each set of houses at a given x position
		for houseSet in houses:
			total += len(houseSet)

		print total
except:
	print "File could not be opened."