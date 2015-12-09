import sys

"""
Problem is pathfinding for shortest path. If you can generate permutations iteratively,
it is possible to only store the smallest calculated distance. After calculating the
distance of one path, compare that to the next distance of the next path. Store the
smallest of the two.

The following solution is crude but it will function for the given input.
"""


class Graph:
    def __init__(self, routes, uniqueLocations, locationIndex, locationCount):
        self.routes = routes
        self.uniqueLocations = uniqueLocations
        self.locationIndex = locationIndex
        self.locationCount = locationCount
        self.paths = []


def distanceBetween(source, dest, graph):
    #For every unique route
    for route in graph.routes:
        #If both the source and destination are in the route then use the distance
        if source in route and dest in route:
            return int(route[2])


def findPaths(start, path, visited, count, graph):
    #Duplicate all lists to create pass by value effect
    #Add the current start position to the current path
    currPath = list(path)
    currPath.append(start)

    #Mark the current start location as visited
    currVisit = list(visited)
    currVisit[graph.locationIndex[start]] = True

    #If there are two locations to compare distance, add that distance to the count
    length = len(currPath)
    if length > 1:
        count += distanceBetween(currPath[-2], currPath[-1], graph)

    #Base case: the locations visited is the same number of locations
    if length == locationCount:
        #Add the path and the distance to the paths list
        graph.paths.append([currPath, count])

    #Recursive case: visit unvisited locations
    else:
        for i in xrange(locationCount):
            if not currVisit[i]:
                findPaths(uniqueLocations[i], currPath, currVisit, count, graph)


try:
    with open(sys.argv[1]) as fileInput:
        #Put each line in the file into a list in the form of [source, dest, distance]
        routes = [line.strip("\n").replace("=", "").replace("to", "").split()
                  for line in fileInput]
except:
    print "File could not be opened."


uniqueLocations = []
#If the location is unique in the source or dest, add it to the list of unique locations
for place in routes:
    if place[0] not in uniqueLocations:
        uniqueLocations.append(place[0])
    if place[1] not in uniqueLocations:
        uniqueLocations.append(place[1])

locationCount = len(uniqueLocations)
locationIndex = {}

#Add the index of every location in uniqueLocations to a dictionary
for i in xrange(locationCount):
    locationIndex[uniqueLocations[i]] = i

graph = Graph(routes, uniqueLocations, locationIndex, locationIndex)

#Find the paths for every start location, the paths are stored in the graph
for start in uniqueLocations:
    visited = [False for location in uniqueLocations]
    visited[locationIndex[start]] = True
    path = []
    count = 0
    findPaths(start, path, visited, count, graph)

#Find the path with the minimum length
currMin = graph.paths[0][1]
resultPath = graph.paths[0][0]
for path in graph.paths:
    if path[1] < currMin:
        currMin = path[1]
        resultPath = path[0]

#Print the path, the distance between each location, and the total distance
dist = 0
print "Shortest Path:", resultPath
for i in xrange(len(resultPath) - 1):
    dist += distanceBetween(resultPath[i], resultPath[i + 1], graph)
    print "Distance between", resultPath[i], "and", resultPath[i + 1], "is",
    print distanceBetween(resultPath[i], resultPath[i + 1], graph)
print "Length:", currMin
