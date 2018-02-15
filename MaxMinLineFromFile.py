"""
Program to Display longest and smallest line from file
"""
def PrintLines(file):
	if file == " ":
		print "Enter file name"
		return -1
		
	fd = open(file)
	line = fd.readline()
	maxLenLine = ""
	minLenLine = ""
	max = min = len(line)
	
	while line:
		length = len(line)
		if length > max:
			max = length
			maxLenLine = line
		elif length < min:
			min = length
			minLenLine = line
			
		line = fd.readline()
		
	print "Max Len Line : ",maxLenLine, max
	print "Min Len Line : ",minLenLine, min
	
if __name__ == "__main__":
	fileName = input("Enter File name : ")
	PrintLines(fileName)