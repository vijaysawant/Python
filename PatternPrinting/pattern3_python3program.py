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
				print(" \t",end="")	#print " \t",	<== python2 syntax
			else:	# (i+j+1 >= row)
				print("*\t",end="")	#print "*\t",	<== python2 syntax
		print("")

if __name__ == "__main__":	
	row = input("Enter num of rows : ")
	pattern(row)