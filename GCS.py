#
#	program to demonstrate conept of GCD of number
#

#! C:\Python\python.exe

def GCD(n1,n2):
	while n1 != n2:
		if n1 > n2:
			n1 = n1 - n2
		else:
			n2 = n2 - n1
	return n1	# or return n2
	
def main():
	n1,n2 = input("Enter 2 nums : ")
	ResGCD = GCD(n1,n2)
	print ("GCD of %d and %d is %d")%(n1,n2,ResGCD)

if __name__ == "__main__":
	main()