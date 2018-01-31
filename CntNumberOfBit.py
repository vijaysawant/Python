"""
Count Number of bits actually counts bits from any number either number is positive or negative.
"""

import sys
def CntBits(Num):
	bit = sys.getsizeof(Num)
	m = 1
	cnt = 0
	while bit != 0:
		if ((Num | m) == Num):
			cnt = cnt + 1
		m = m << 1
		bit = bit - 1
		
	print ("Num of 1's : ",cnt)
    
if __name__ == "__main__":
	No = eval(input("Enter number : "))
	CntBits(No)