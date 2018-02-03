'''
	WAP to accept Num, position, NumOfBits from user and Toggle respective bits and return result
	pos = 5, NumOfBits  = 4, Num = 218
			|----->
	0 1 1 0 1 1 0 1 0
   ^
	0 0 0 0 1 1 1 1 0
----------------------
	0 1 1 0 0 0 1 0 0
	
'''
def ToggleBit(num, pos, numOfBit):
	if pos >= numOfBit:
		x = (1 << numOfBit) - 1
		x = x << (pos - numOfBit)
		return num ^ x
	return -1

if __name__ == "__main__":
	num, pos, numOfBit = input("Enter num, position, Num of bits : ")
	print "Original : ",bin(num)
	print "after Toggle : ",bin(ToggleBit(num, pos, numOfBit))