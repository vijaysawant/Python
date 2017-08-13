#
#	Program to check no is armstrong or not
#

#! C:\Python\python.exe

def CheckArmstrong(no):
	temp = no
	LD = 0
	sum = 0
	cube = 0
	while no != 0:
		LD = no%10
		cube = (LD*LD*LD)
		sum  = sum + cube
		no = no / 10
		
	if temp == sum:
		print "Armstrong"
	else:
		print "Not Armstrong"
	
if __name__ == '__main__':
	no = input("ENter Number : ")
	res = CheckArmstrong(no)
	
	
	
	
	