'''
input = 4

      *
    * *
  * * *
* * * *

'''
def pattern(row):
	for i in range(0,row):
		for j in range(0,row):
		
			if (i+j+1 < row):
				print " \t",
			else:	# (i+j+1 >= row)
				print "*\t",
		print

if __name__ == "__main__":	
	row = input("Enter num of rows : ")
	pattern(row)