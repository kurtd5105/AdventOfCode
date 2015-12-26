import sys
import itertools
import operator

try:
	with open(sys.argv[1]) as fileInput:
		boxes = [int(line.strip()) for line in fileInput]
except:
	print "File could not be opened."

boxes = boxes[::-1]


def matchBucket(bucket, pool, count):
	target = sum(bucket)
	size = len(pool)
	buckets = [[] for x in xrange(count)]
	newPool = list(pool)
	#Increase the search size
	for i in range(1, size):
		buckets = [[] for x in xrange(count)]
		newPool = list(pool)
		#For every needed bucket
		for c in xrange(count):
			amount = i
			#If it's the last bucket then only check for the required amount of numbers
			if c + 1 == count:
				amount = len(newPool)
			#For every combination of numbers check if the sum is the target sum
			for numbers in itertools.combinations(newPool, amount):
				if sum(numbers) == target:
					#Add the numbers into the bucket
					buckets[c] = list(numbers)
					#Remove the numbers from the pool
					newPool = [num for num in newPool if (num not in buckets[c])]
					break
		#If all buckets are full and the pool is empty
		if [] not in buckets and newPool == []:
			return buckets, newPool
	return buckets, pool

buckets = [[], [], []]

#For every starting pool size
#Note that the first pool should have the least elements, and thus the largest in size.
#Therefore, the boxes are sorted in decreasing order and the first pool is taken from the
#start.
for i in range(6, len(boxes) - 1):
	pool = list(boxes)
	buckets = [[], [], []]
	#For every combination of the initial pool
	for numbers in itertools.combinations(pool, i):
		buckets[0] = [x for x in numbers]
		currPool = [num for num in pool if (num not in buckets[0])]
		newBuckets, currPool = matchBucket(buckets[0], currPool, 2)
		buckets[1] = newBuckets[0]
		buckets[2] = newBuckets[1]
		#If a valid result came back break
		if buckets[1] != [] and buckets[2] != [] and currPool == []:
			break
	#If the result was valid then break
	if sum(buckets[0]) == sum(buckets[1]) and sum(buckets[1]) == sum(buckets[2]):
		break

print "Final match", buckets, [sum(buckets[x]) for x in xrange(len(buckets))]
print "Quantum Entanglement:", reduce(operator.mul, buckets[0])
