def ReadFile(fileName):
	fd = open(fileName)
	line = fd.readline()
	
	while line != "":
		print line,
		line = fd.readline()
'''	
# OR we can write using readlines() function
	fd.seek(0)
	x = fd.readlines()
	for line in x:
		print line,
'''
def CreateFile(FileName):
	fd = open(FileName, "w")
	
if __name__ == "__main__":
	fileName = input("Enter File name : ")
	ReadFile(fileName)
