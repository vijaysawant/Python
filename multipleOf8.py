
def multipleOf8(no):
	if (no & 7 == 0):
		print "num is multiple of 8"
	else:
		print "num is not multiple of 8"
	
	
def CountOnceInNum(no):
	cnt = 0
	mask = 1
	if no == 0:
		print "Number of 1's are zero"
	
	while mask < no:
		if no & mask == 1:
			cnt = cnt + 1
		mask = mask << 1
		
	print "Num of 1's are : ",cnt
	
	
if __name__ == '__main__':
	num = input("Enter num : ")
	#multipleOf8(num)
	CountOnceInNum(num)
	