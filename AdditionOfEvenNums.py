#
#	Program to print addtiton of even nums
#

#! C:\Python\python.exe

no = input("Enter value of n : ")
sum = 0
i = 0

while i <= no:
	if i%2 == 0:
		sum += i
	i+=1

print("Sum of even nums from 0 to %d is %d"%(no,sum))
