'''
Program to implements own readline function.
'''
def MyReadLine(fd,NumOfLines):
	if NumOfLines < 1:
		return None
	while NumOfLines != 0:
		line = fd.readline()
		print line,
		NumOfLines -= 1
	

if __name__ == "__main__":
	fileName = input("Enter File name : ")
	numOfLines = input("How many lines to read : ")
	fd = open(fileName,"r")
	MyReadLine(fd,numOfLines)