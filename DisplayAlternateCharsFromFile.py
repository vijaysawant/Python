"""
Program to display alternate N charactors from string
"""

def DisplyChars(FileName, NumOfChar):
	if FileName == "":
		print "Enter File name"
		return None
	fd = open(FileName)
	
	while 1:
		data = fd.read(NumOfChar)
		if data == "":
			break
		else:
			print data,
			fd.seek(NumOfChar,1)



if __name__ == "__main__":
	fileName = input("Enter file name : ")
	NumOfChar = input("How many charactors you want to display : ")
	DisplyChars(fileName, NumOfChar)