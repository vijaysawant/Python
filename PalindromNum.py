#
#	program to check number is palindrom or not
#

#! C:\Python\python.exe

def Palindrom(no):
	LD = 0
	rev = 0
	while no != 0:
		LD = no % 10
		rev = rev * 10 + LD
		no = no / 10
	return rev	
	
def main():	
	no = input("Enter Num : ")
	ans = Palindrom(no)
	if no == ans:
		print "Palindrom"
	else:
		print "Not Palindrom"

if __name__ == "__main__":
	main()