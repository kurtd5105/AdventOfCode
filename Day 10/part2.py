string = "1113122113"

#Perform look-and-say 40 times
for i in xrange(50):
    newString = []
    prev = string[0]
    count = 1
    for char in string[1:]:
        #If the current char is the same as the last increase the count
        if char == prev:
            count += 1
        #Otherwise append the look-and-say for the previous char and its count and restart
        else:
            newString.append(str(count) + prev)
            count = 1
            prev = char
    #Add the look-and-say for the last character since it is missed in the loop
    if count == 1:
        newString.append("1" + string[-1])
    else:
        newString.append(str(count) + string[-1])
    #Combine the newString list into a single string
    string = "".join(newString)

print len(string)
