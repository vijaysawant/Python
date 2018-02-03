def turnOFfBit(num, pos, numOfBit):
	if pos >= numOfBit:
		x = (1 << numOfBit) - 1
		x = x << (pos - numOfBit)
		x = ~x
		return num & x
	return -1
	
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
	
def check2sPower(Num):
	m = 1
	cnt = 0
	while m < Num:
		if Num & m == 1:
