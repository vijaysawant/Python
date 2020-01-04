'''
WAP to Read File and Create Dictionary using data from that file
'''

def CreateDictionary(FileName):
	fd = open(FileName,"r")
	resDict = {}
	line = fd.readline()
	while line != "":
		data = line.split("=")
		resDict[data[0]] = data[1]
		line = fd.readline()
	print "Dict : ",resDict
	return None

if __name__ == "__main__":
	fileName = input("Enter File name : ")
	res = CreateDictionary(fileName)
	print res