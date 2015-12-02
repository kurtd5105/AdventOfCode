import sys
try:
    with open(sys.argv[1]) as fileInput:
        #Convert the input to a series of 1 or -1 if the char is ( or )
        converted = [1 if char == '(' else -1 for char in fileInput.read()
             if char == '(' or char == ')']
        
        total = 0
        pos = 0
        #Santa is in the basement when the total is negative
        while total >= 0:
            total += converted[pos]
            pos += 1
        print pos
except:
    print "File could not be opened."
