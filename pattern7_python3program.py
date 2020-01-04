"""
Enter charactor and Number of rows : 'A',4
A
A A
A A A
A A A A
"""

def patter(chr,row):
	for i in range(1,row+1):	# now i is 1
		#ch = chr
		for j in range(1,i+1):
			print("%c\t"%chr,end="")	# here , comma is use to avoid new line
			#ch += 1
		print("")				# here print is use to print new line
		
		
if __name__ == '__main__':
	chr,row = eval(input("Enter character and Number of rows : "))
	patter(chr,row)		
