import sys
import itertools

try:
	with open(sys.argv[1]) as fileInput:
		containers = [int(line.strip()) for line in fileInput]
except:
	print "File could not be opened."


length = len(containers)
total = 0
limit = -1

#Find groups of the minumum amount of bottles that have exactly 150L storage
for i in xrange(length):
	if limit == -1 or limit == i:
		for items in itertools.combinations(containers, i):
			if sum(items) == 150:
				if limit == -1:
					limit = i
				total += 1

print total
