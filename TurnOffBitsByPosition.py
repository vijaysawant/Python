'''
	WAP to accept Num, position, NumOfBits from user and TurnOFF respective bits and return result

	pos = 5, NumOfBits  = 4, Num = 218
			|----->
	0 1 1 0 1 1 0 1 0
	
	0 0 0 1 0 0 0 0 0	(1 << numOfBit)
	0 0 0 0 0 1 1 1 1	x = (1 << numOfBit) - 1
	0 0 0 0 1 1 1 1 0	x << (pos - numOfBit)
	1 1 1 1 0 0 0 0 1	~x

	0 1 1 0 1 1 0 1 0	Num
   &
	1 1 1 1 0 0 0 0 1	x
-----------------------
	0 1 1 0 0 0 0 0 0

'''

def turnOFfBit(num, pos, numOfBit):
	if pos >= numOfBit:
		x = (1 << numOfBit) - 1
		x = x << (pos - numOfBit)
		x = ~x
		return num & x
	return -1

if __name__ == "__main__":
	num, pos, numOfBit = input("Enter num, position, Num of bits : ")
	print "Original : ",num
	print "after turnoff : ",turnOFfBit(num, pos, numOfBit)