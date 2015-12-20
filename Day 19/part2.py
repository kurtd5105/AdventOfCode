import sys
import re

"""
My initial attempt was a BFS with a priority queue, but a particular string of 23 length
could not be compressed further, and halted all progress in the BFS. A greedy search
is clearly not the best solution to this problem. Fortunately a reddit user simplified
the problem:
https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju

So the equation for finding the solution is:
count(tokens) - count(Rn and Ar) - 2*count(Y) - 1
"""

try:
	with open(sys.argv[1]) as fileInput:
		replacements = [line.strip() for line in fileInput]
except:
	print "File could not be opened."

string = replacements[-1]
tokens = 0

rRnAr = re.compile("((Rn)|(Ar))")
rY = re.compile("(Y)")

#Count the amount of Rn, Ar and Y molecules
RnAr = len(rRnAr.findall(string))
Y = len(rY.findall(string))

#Count the amount of molecules
for char in string:
	if char.isupper():
		tokens += 1

#count(tokens) - count(Rn and Ar) - 2*count(Y) - 1
print tokens - (RnAr + (2 * Y) + 1)
