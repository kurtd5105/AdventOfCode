import sys

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

limit = 2503
distances = []

#Calculate the distance that each reindeer travels in 2503 seconds
for reindeer in parsedData:
	time = 0
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
			if timeCycle < reindeer[3]:
				timeCycle += 1
				time += 1
			else:
				flying = True
				timeCycle = 0

	distances.append(distance)

#Print the largest distance travelled
print max(distances)
