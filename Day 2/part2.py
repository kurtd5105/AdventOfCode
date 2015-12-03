import sys

def minRibbon(prism):
	a = prism[0] * prism[1]
	b = prism[0] * prism[2]
	c = prism[1] * prism[2]

	#Based on the smallest area, return the smallest dimensions
	if a < b:
		if a < c:
			return [prism[0], prism[1]]
		else:
			return [prism[1], prism[2]]
	elif b < c:
		return [prism[0], prism[2]]
	return [prism[1], prism[2]]

try:
	with open(sys.argv[1]) as fileInput:
		#Read the dimensions in axbxc format and convert to a list in the form of 
		#[a, b, c] as integers
		formatted = [map(int, substring) for substring in 
						(string.split('x') for string in fileInput.read().split())]
		total = 0
		for prism in formatted:
			#Get the ribbon dimensions
			ribbon = minRibbon(prism)
			#Total needed is 2 x the minimum perimeter + l * w * h
			total += (2 * sum(ribbon)) + prism[0] * prism[1] * prism[2]

		print total
except ValueError:
	print "File contains invalid data."
except:
	print "File could not be opened."