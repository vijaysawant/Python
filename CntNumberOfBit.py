# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:25:40 2018

@author: vijay.sawant
"""

import sys
def CntBits(Num):
	bit = sys.getsizeof(Num)
	#print("bits : ",bit)
	m = 1
	cnt = 0
	while bit != 0:
		if ((Num | m) == Num):
			#print ("found ",cnt)
			cnt = cnt + 1
		m = m << 1
		bit = bit - 1
		#print("Remaining bits : ",bit)
		
	print ("Num of 1's : ",cnt)
	
def FindNumberOfOnce(Num):
	mask = 1
	cnt = 1
	bit = sys.getsizeof(Num)
	while(Num > mask):
		if Num | mask == Num:
			cnt += 1
		mask = mask << 1

	print ("+ve num : ",cnt)
	
    
if __name__ == "__main__":
	No = eval(input("Enter number : "))
	CntBits(No)
	#FindNumberOfOnce(No)
	