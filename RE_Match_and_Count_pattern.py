
import re
def CountOccurencesOfPattern(pattern, data):
	count = 0

if __name__ == "__main__":
	pattern = input("Enter pattern :")
	data = input("Enter input data string :")
	
	result = 0
	result = CountOccurencesOfPattern(pattern, data)
	print "{0} found {1} times in {}".format(pattern, result, data)