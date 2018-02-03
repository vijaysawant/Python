'''
	WAP to accept Num, position, NumOfBits from user and TurnON respective bits and return result
	pos = 5, NumOfBits  = 4, Num = 218
			|----->
	0 1 1 0 1 1 0 1 0
   |
	0 0 0 0 1 1 1 1 0
----------------------	
	0 1 1 0 1 1 1 1 0
'''
def turnONBit(num, pos, numOfBit):
	if pos >= numOfBit:
		x = (1 << numOfBit) - 1
		x = x << (pos - numOfBit)
		return num | x
	return -1

if __name__ == "__main__":
	num, pos, numOfBit = input("Enter num, position, Num of bits : ")
	print "Original : ",num
	print "after turnON : ",turnONBit(num, pos, numOfBit)