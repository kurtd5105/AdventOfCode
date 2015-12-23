import sys

try:
	with open(sys.argv[1]) as fileInput:
		program = [line.strip().replace(',', '').split() for line in fileInput]
except:
	print "File could not be opened."

#Init the program counter
programCounter = -1

#Set the end of program
EOP = len(program)

register = {'a': 1, 'b': 0}
instructions = {}

#Process the instructions while the program counter doesn't overflow the program
while programCounter < EOP - 1:
	programCounter += 1
	instruction = program[programCounter]
	#Store half of the register back in the register
	if instruction[0] == "hlf":
		register[instruction[1]] /= 2
	#Store three times the register back in the register
	elif instruction[0] == "tpl":
		register[instruction[1]] *= 3
	#Increment the register
	elif instruction[0] == "inc":
		register[instruction[1]] += 1
	#Jump to another place in the program memory
	elif instruction[0] == "jmp":
		programCounter += int(instruction[1]) - 1
	#Jump to another place in the program memory if a register is even
	elif instruction[0] == "jie":
		if register[instruction[1]] % 2 == 0:
			programCounter += int(instruction[2]) - 1
	#Jump to another place in the program memory if a register is one
	elif instruction[0] == "jio":
		if register[instruction[1]] == 1:
			programCounter += int(instruction[2]) - 1

print register['b']
