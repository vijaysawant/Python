'''
input = 4

		  *
		* *
	  * * *
	* * * *
	* * * *
	  * * *
		* *
		  *
'''
def pattern(row):
	for i in range(0,row):		# loop for number of rows,now we only consider 4 rows 
		for j in range(0,row):	# loop for number of colomns
			if (i+j+1 < row):	# if statement of print spaces
				print(" \t",end="")
			else:	# (i+j+1 >= row)	# for printing stars
				print("*\t",end="")
		print("")
# now consider mirror image i.e next 4 rows
	for i in range(row,row*2):
		for j in range(0,row):
			if (i - j <= row):	# here i > j
				print("*\t",end="")
			else:	# (i - j > row)		# for printing spaces
				print(" \t",end="")
		print("")
				
		
if __name__ == "__main__":	
	row = eval(input("Enter num of rows : "))
	pattern(row)