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
			print "*\t",
		print

if __name__ == "__main__":	
	row = input("Enter num of rows : ")
	pattern(row)