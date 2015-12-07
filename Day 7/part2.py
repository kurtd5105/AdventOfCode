import sys

INT_LIMIT = 65535


def andi(a, b):
	return a & b


def ori(a, b):
	return a | b


def lsli(a, b):
	return a << b


def lsri(a, b):
	return a >> b


def comi(a):
	return INT_LIMIT - a


try:
	with open(sys.argv[1]) as fileInput:
		#Take each line from fileInput and split it up at the spaces
		instructions = [line.split() for line in fileInput]
except:
	print "File could not be opened."

instructionSet = {
	"AND": andi,
	"OR": ori,
	"LSHIFT": lsli,
	"RSHIFT": lsri,
	"NOT": comi
}

#The result from part 1 is the override for b
wires = {'b': 3176}

parsedInstructions = []
for instruction in instructions:
	operator = None
	result = 0
	data = []

	#Parse every instruction for later processing in the form [operator, operands, dest]
	#Ignore ->, as it is implied
	for part in instruction[:-1]:
		if part in instructionSet:
			operator = instructionSet[part]
		elif part != "->":
			if part.isdigit():
				data.append(int(part))
			else:
				#Set the wire to uninitialized
				if part not in wires:
					wires[part] = -1
				data.append(part)
	parsedInstructions.append([operator, data, instruction[-1]])

prevLength = 0
while len(parsedInstructions) != prevLength:
	length = len(parsedInstructions)
	prevLength = length
	#print length
	for i in xrange(length):
		executable = True

		#Check to see if the input is >= 0
		for j in xrange(len(parsedInstructions[i][1])):
			#If the data is a string then it represents a wire and not a value directly
			if isinstance(parsedInstructions[i][1][j], str):
				temp = wires[parsedInstructions[i][1][j]]
				if temp == -1:
					executable = False
					break
				else:
					parsedInstructions[i][1][j] = temp

		if executable:
			#Override b to the result from part 1
			if parsedInstructions[i][2] != 'b':
				#If there isn't an operator then simply store the data
				if parsedInstructions[i][0] is None:
					wires[parsedInstructions[i][2]] = sum(parsedInstructions[i][1])
				else:
					wires[parsedInstructions[i][2]] = parsedInstructions[i][0](*parsedInstructions[i][1])
				parsedInstructions.pop(i)
				#Break after removing an instruction
				break

if "a" in wires:
	print "Wire 'a':", wires["a"]
else:
	print "'a' not in wires..."
	print wires
