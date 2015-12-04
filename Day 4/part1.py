import hashlib

key = "iwrupvqb"
#Create an MD5 hasher
hasher = hashlib.md5()
#Add the key to the hasher
hasher.update(key)

result = ""
i = 0
while result[0:5] != "00000":
	#Copy the hasher so that we can add the index to the end without making a new hasher
	h = hasher.copy()
	h.update(str(i))
	#Get the hexadecimal hash of the key + i
	result = h.hexdigest()
	#Useful if you want progress updates
	#if i % 10000 == 0:
	#	print "\tHashing index", i, "result:", result
	i += 1

#Print out the index and its hash
print "Result: ", (i - 1)
hasher.update(str(i - 1))
print hasher.hexdigest()
