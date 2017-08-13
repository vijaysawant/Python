#
#	program to print reverse number of given number
#

#! C:\Python\python.exe

def RevOfNum(no):
	LD = 0
	rev = 0
	while no != 0:
		LD = no % 10
		rev = rev * 10 + LD
		no = no / 10
		
	return rev

def main():	
	no = input("Enter Num : ")
	ans = RevOfNum(no)
	print ans

if __name__ == "__main__":
	main()