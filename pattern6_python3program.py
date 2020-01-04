"""
Enter num of rows : 4
*
*	*	*
*	*	*	*	*
*	*	*	*	*	*	*
"""

def pattern(r):
	for i in range(0,r):
		for j in range(0,2*i+1):
			print("*\t",end="")
		for j in range(0,r-i-1):
			print(" \t",end="")
		print("")
		
		

if __name__ == "__main__":	
	row = eval(input("Enter num of rows : "))
	pattern(row)