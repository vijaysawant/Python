'''
WAP to read txt file data and create Dictonary from that information.
'''

def CreateDict(FileName):
	for ln in FileName.readlines():
		ln.split("=")
		print ln[0],ln[1],ln[2],ln[3]

def main():
	fp = open("InputFileToCreateDict.txt")
	if fp == None:
		print "File not found"
	else:
		#print "File found"
		result = CreateDict(fp)
		#print result
		
if __name__ == "__main__":
	main()