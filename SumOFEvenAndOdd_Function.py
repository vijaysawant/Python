#
#	Program to demonstrate concept of Sum of Even and Odd numbers using function
#

#! C:\Python\python.exe

def SumEvenOdd(lb,ub):
	SumEven = 0
	SumOdd = 0
	
	if lb >= ub:
		print "lower and upper bound should be proper"
		return 1,1
	while lb <= ub:
		if lb % 2 == 0:
			SumEven += lb
		else:
			SumOdd += lb
			
		lb += 1
	return SumEven,SumOdd

def main():
	lb,ub = input("Enter lower bound and upper bound, comma seperately..!")
	SE,SO = SumEvenOdd(lb,ub)
	if SE == SO == 1:
		pass
	else:
		print "Sum of\nEven = %d\tOdd = %d"%(SE,SO)
		
if __name__ == '__main__':	# Note that it is not main function
	main()
	
	