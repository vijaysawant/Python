"""
implement own re.findall()
"""

import re


def findAll(pattern, data):
	allIndices = []
	index = 0
	x = re.search(pattern, data)
	
	while x != None:
		allIndices.append((x.start() + index, x.end() + index))
		index += x.end()
		data = data[x.end():]
		x = re.search(pattern, data)
		
	return allIndices

	
	
	
if __name__ == "__main__":
	pattern = input("Enter pattern :")
	data = input("Enter string :")
	
	result = findAll(pattern, data)
	print result

"""
>>> x = re.findall("h","zxchellohi")
>>> x
['h', 'h']
>>> x = re.findall("l","zxchellohi")
>>> x
['l', 'l']
>>> x = re.findall("a","zxchellohi")
>>> x
[]
>>> x = re.findall("e","zxchellohi")
>>> x
['e']


Output -
	Enter pattern :"h"
	Enter string :"ahshellohi"
	[(1, 2), (3, 4), (8, 9)]
"""