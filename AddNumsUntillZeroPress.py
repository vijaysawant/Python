#
#	program to keep on adding numbers untill user enters 0
#	and print sum of all numbers
#

#! C:\Python\python

iSum = 0
iNum = input("Enter Nums till press 0\nNumber :")

while iNum != 0:
	iSum += iNum
	iNum = input(":")
	continue
	
print"Sum of nums = %d"%(iSum)
