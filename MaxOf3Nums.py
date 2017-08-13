#
#	Program to print maximum of 3 nums
#

#! C:\Python\python.exe

def MaxOfNums(n1,n2,n3):
	if n1 > n2 and n2 > n3:
		print("%d is Max"%n1)
	elif n1 < n2 and n2 > n3:
		print("%d is Max"%n2)
	else:
		print("%d is Max"%n3)
	return

n1,n2,n3 = input("Enter 3 nums comma seperately : ")

MaxOfNums(n1,n2,n3)