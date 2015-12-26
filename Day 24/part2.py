import sys
import itertools
import operator

try:
	with open(sys.argv[1]) as fileInput:
		boxes = [int(line.strip()) for line in fileInput]
except:
	print "File could not be opened."

boxes = boxes[::-1]
size = len(boxes)


def matchBucket(bucket, pool, bucketsLeft):
	target = sum(bucket)
	size = len(pool)
	currBucket = []
	newPool = list(pool)
	#If the pool is empty then a match can't be made
	if pool == []:
		return bucket, bucket
	amount = len(bucket)
	#If more numbers are required than there are in the pool then a match can't be made
	if amount > len(pool):
		return bucket, bucket
	#If it's the last bucket then only check for the required amount of numbers
	if bucketsLeft == 1:
		if sum(newPool) == target and len(newPool) >= amount:
			#print newPool, 1
			return [list(newPool)], []
		else:
			return [], newPool
	#For every combination of numbers check if the sum is the target sum
	while amount <= size:
		for numbers in itertools.combinations(newPool, amount):
			if sum(numbers) == target:
				#Add the numbers into the bucket
				currBucket = list(numbers)
				#Remove the numbers from the pool
				newPool = [num for num in newPool if (num not in currBucket)]
				newBuckets = []
				newBuckets, newPool = matchBucket(currBucket, newPool, bucketsLeft - 1)
				#If the whole pool was used up then return the buckets
				if newPool == []:
					temp = [currBucket]
					for b in newBuckets:
						if b != []:
							temp.append(b)
					return temp, newPool
		amount += 1
	return [[] for x in xrange(bucketsLeft)], pool

buckets = [[], [], [], []]
minEntanglement = 1e100
minBucket = []

#For every starting pool size
#Note that the first pool should have the least elements, and thus the largest in size.
#Therefore, the boxes are sorted in decreasing order and the first pool is taken from the
#start.
for i in range(5, len(boxes) - 1):
	pool = list(boxes)
	buckets = [[], [], [], []]
	#For every combination of the initial pool
	for numbers in itertools.combinations(pool, i):
		buckets[0] = [x for x in numbers]

		#If the bucket doesn't start with the largest value and there is a min entanglement found
		if buckets[0][0] != boxes[0] and minEntanglement < 1e100:
			break
		currPool = [num for num in pool if (num not in buckets[0])]
		newBuckets, currPool = matchBucket(buckets[0], currPool, 3)
		buckets[1] = newBuckets[0]
		buckets[2] = newBuckets[1]
		buckets[3] = newBuckets[2]
		#If a valid result came back
		if [] not in buckets and currPool == []:
			lengths = [len(bucket) for bucket in buckets]
			#If the smallest bucket is the first and the whole pool was used
			if min(lengths) == lengths[0] and sum(lengths) == size:
				entanglement = reduce(operator.mul, buckets[0])
				if entanglement < minEntanglement:
					minEntanglement = entanglement
					minBucket = list(buckets)
					print "New bucket found with min entanglement", reduce(operator.mul, minBucket[0])
		pool = list(boxes)
		buckets = [[], [], [], []]
	#If the result was valid then break
	if minEntanglement < 1e100:
		break
	if len(buckets[0]) >= 1:
		if buckets[0][0] != boxes[0]:
			break

print "Final match", minBucket, [sum(minBucket[x]) for x in xrange(len(minBucket))]
print "Quantum Entanglement:", reduce(operator.mul, minBucket[0])
