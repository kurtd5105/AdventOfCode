import sys

def minArea(prism):
	a = prism[0] * prism[1]
	b = prism[0] * prism[2]
	c = prism[1] * prism[2]

	#Return the smallest area of the prism
	if a < b:
		if a < c:
			return a
		else:
			return c
	elif b < c:
		return b
	return c

try:
	with open(sys.argv[1]) as fileInput:
		#Read the dimensions in axbxc format and convert to a list in the form of 
		#[a, b, c] as integers
		formatted = [map(int, substring) for substring in 
						(string.split('x') for string in fileInput.read().split())]
		total = 0
		for prism in formatted:
			#2*l*w + 2*w*h + 2*h*l + min area
			total += 2 * ((prism[0] * prism[1]) + (prism[1] * prism[2]) + 
				(prism[2] * prism[0])) + minArea(prism)

		print total
except ValueError:
	print "File contains invalid data."
except:
	print "File could not be opened."