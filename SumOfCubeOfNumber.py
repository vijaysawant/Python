#
#	Program to print sum of cube of a number
#

#! C:\Python\python.exe

def SumOfCube(no):
	LD = 0
	sum = 0
	cube = 0
	while no != 0:
		LD = no%10
		cube = (LD*LD*LD)
		sum  = sum + cube
		no = no / 10
		
	return sum
	
if __name__ == '__main__':
	no = input("ENter Number : ")
	res = SumOfCube(no)
	print res