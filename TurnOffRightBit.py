"""turn off right most bit_length
ex = 110000000	=	384
	 100000000	=	256
"""

def turnOFfBit(Num):
	m = 1
	res = 0
	print "original : ",Num
	while m < Num:
		if (Num & m != 0):
			break
		m = m << 1
	res = Num ^ m
	#res = Num & ~m
	#toggle mask bit, 1 to 0
	print "after turningOff : ",res
		
if __name__ == "__main__":
	num = input("Enter num : ")
	turnOFfBit(num)