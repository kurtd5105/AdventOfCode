import sys

try:
    with open(sys.argv[1]) as fileInput:
        #Put each line in the file into an array
        lines = [line.strip("\n") for line in fileInput]
except:
    print "File could not be opened."

formattedLines = []
total = 0
for line in lines:
    #Convert the string to its parsed form
    formattedLines.append(line[1:-1].decode('string_escape'))

for i in xrange(len(formattedLines)):
    #Subtract the length of the parsed string from the literal and add to the total
    total += len(lines[i]) - len(formattedLines[i])

print total
