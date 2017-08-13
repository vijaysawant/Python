#
#	Program to print minimum of 3 nums
#

#! C:\Python\python.exe


def MinOfNums(n1,n2,n3):
	if n1 < n2 and n2 < n3:
		print("%d is Min"%n1)
	elif n1 > n2 and n2 < n3:
		print("%d is Min"%n2)
	else:
		print("%d is Min"%n3)
	return

print"Finding out minimum of 3 Nums"
n1,n2,n3 = input("Enter 3 nums comma seperately : ")
MinOfNums(n1,n2,n3)
