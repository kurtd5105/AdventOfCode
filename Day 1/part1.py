import sys

try:
    with open(sys.argv[1]) as fileInput:
        #Convert the input to a series of 1 or -1 if the char is ( or )
        #Sum the result of this conversion
        print sum([1 if char == '(' else -1 for char in fileInput.read()
             if char == '(' or char == ')'])
except:
    print "File could not be opened."
