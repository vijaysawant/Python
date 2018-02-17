# print file in reverse order
def DisplayFile(fd):
	data = fd.read(1)
	if data:
		DisplayFile(fd)
	print data,
	return
# or
# Print reverse lines file
def ReveseLineDisplay(fd):
	line = fd.readline()
	if line == "":
		return
	ReveseLineDisplay(fd)
	print line

if __name__ == "__main__":
	fileName = input("Enter File name : ")
	fd = open(fileName)
	print "File in revser order : "
	DisplayFile(fd)
	print "File lines in Reverse order : "
	fileName = input("Enter File name : ")
	fd = open(fileName)
	ReveseLineDisplay(fd)
	