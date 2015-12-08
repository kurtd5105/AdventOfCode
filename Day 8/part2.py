import sys

try:
    with open(sys.argv[1]) as fileInput:
        #Put each line in the file into an array
        lines = [line.strip("\n") for line in fileInput]
except:
    print "File could not be opened."

total = 0
escaped = ["\\", '"']
for line in lines:
    #Sum each character in the line, and  again if there is a character to escape
    for char in line:
        total += 1
        if char in escaped:
            total += 1
    #Add 2 for the encompassing quotes
    total += 2
    #Subtract the initial string length
    total -= len(line)

print total
