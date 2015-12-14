import sys


def getNextDist(reindeer):
	"""Iterator to Calculate the distance that each reindeer travels in 2503 seconds"""
	limit = 2503
	time = 0
	prevTime = 0
	timeCycle = 0
	distance = 0
	flying = True
	while time < limit:
		#If it's flying then it's moving
		if flying:
			#If the reindeer isn't tired and doesn't need to stop
			if timeCycle < reindeer[2]:
				#Increase the distance by its speed
				distance += reindeer[1]
				timeCycle += 1
				time += 1
			else:
				flying = False
				timeCycle = 0
		else:
			#If the reindeer is still tired
				flying = True
				timeCycle = 0
		#If it is a unique distance travelled then yield the disance
		if time != prevTime:
			yield distance
		prevTime = time

try:
	with open(sys.argv[1]) as fileInput:
		reindeerData = [line.strip() for line in fileInput]
except:
	print "File could not be opened."

parsedData = []

#Parse each line so that it contains the reindeer name, speed, cooldowns (2)
for line in reindeerData:
	line = line.replace(" can fly", "").replace(" km/s for", "")
	line = line.replace(" seconds, but then must rest for", "")
	line = line.split(" ")[:4]
	line[1] = int(line[1])
	line[2] = int(line[2])
	line[3] = int(line[3])
	parsedData.append(list(line))

distances = {}
scores = {}

#Create an entry for every reindeer and containing a list of its distance every second
for reindeer in parsedData:
	distances[reindeer[0]] = [dist for dist in getNextDist(reindeer)]
	scores[reindeer[0]] = 0

limit = 2503

#Award score for the leader(s)
for i in xrange(limit):
	values = {}
	#Create a keyword for each reindeer's distance, with a list of reindeer with that value
	for reindeer in distances:
		#If the value doesn't exist yet then add it with the reindeer as its key
		if distances[reindeer][i] not in values:
			values[distances[reindeer][i]] = [reindeer]
		else:
			values[distances[reindeer][i]].append(reindeer)

	#Get the max distance travelled
	maxDist = max([value for value in values])
	leads = values[maxDist]

	#Increase the score for every leader
	for leader in leads:
		scores[leader] += 1

scoreValues = []
#Put all the scores into a list
for key, value in scores.iteritems():
	scoreValues.append(value)

#Print the maximum score obtained
print max(scoreValues)
