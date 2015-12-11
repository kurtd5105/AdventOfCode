import re


def unsuitable(string, m):
	#If there are at least 2 groups of repeated letters
	if len(m.findall("".join(string))) >= 2:
		if 'i' not in string and 'o' not in string and 'l' not in string:
			strArray = [ord(char) for char in string]
			i = 0
			length = len(string)
			while i + 2 < length:
				#If there are 3 letters in increasing order then the string is suitable
				if range(strArray[i], strArray[i] + 3) == strArray[i:i + 3]:
					return False
				i += 1
	return True


def incrementString(string, length):
	i = -1
	temp = chr(ord(string[-1]) + 1)

	#Carry over
	if temp > 'z':
		while temp > 'z':
			#Set the overflowed character back to 'a'
			string[i] = 'a'
			i -= 1

			#Insert a to the start of the list if there is an overflow
			if i < length:
				string.insert(0, 'a')
				break

			#Try to add the carry to the next letter
			temp = chr(ord(string[i]) + 1)
			if temp <= 'z':
				string[i] = temp
	else:
		string[-1] = temp

#Turn the string into a list
string = list("hepxcrrq")
m = re.compile("((\w)\\2)")

i = 0
length = -len(string)

while i <= 1:
	incrementString(string, length)
	while unsuitable(string, m):
		incrementString(string, length)
	i += 1

print "".join(string)
