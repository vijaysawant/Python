'''
input - 4
* * * *
* * * 
* * 
*
'''

def pattern(row):
	for i in range(0,row):
		for j in range(0,row-i):
			print("*\t", end="")	#print "*\t",	<== python2 syntax
		print("")					#print			<== python2 syntax

if __name__ == "__main__":	
	row = eval(input("Enter num of rows : "))
	pattern(row)