##  Program to read data from file  ##

#! C:\Python\python.exe

f = open("file.txt")
line = f.readline()
while line:
	print line,
	line = f.readline()
f.close()

'''
# above program uing for loop
for line in open("file.txt"):
	print line,
'''