'''
WAP to accept 2 number from user,also accept position, and NumOfBits to be swap

pos = 5, NumOfBits = 4
			   |-----|
Num1 = 0 1 1 0 1 1 0 0 1	= 217
Num2 = 0 1 1 0 0 0 1 1 0	= 198

Num1 = 0 1 1 0 0 0 1 1 1	= 199
Num2 = 0 1 1 0 1 1 0 0 0	= 216
			   |-----|
'''
def SwapBit(Num1, Num2, pos, numOfBit):
	if numOfBit <= pos:
		x = (1 << numOfBit) - 1
		x =  

if __name__ == "__main__":
	Num1, Num2 = input("Enter two numbers : ")
	pos, numOfBit = input("Enter Bit position, Num of bits to swap : ")
	print "Original : "
	print bin(Num1),bin(Num2)
	print "after Swapped : ",bin(SwapBit(Num1, Num2, pos, numOfBit))