'''
Enter num of rows : 4
   *
  ***
 *****
*******
'''

def pattern(r):
	for i in range(0,r):
		for j in range(0,r-i-1):	# this loop for top left spaces
			print(" \t",end="")
		for j in range(0,2*i+1):	# this loop for all stars
			print("*\t",end="")
		print("")

if __name__ == "__main__":	
	row = eval(input("Enter num of rows : "))
	pattern(row)