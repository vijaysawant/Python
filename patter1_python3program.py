"""
input = 4
*
* *
* * *
* * * * 
"""

def patter(row):
	i = 0
	j = 0
	for i in range(1,row+1):	# now i is 1
		for j in range(1,i+1):
			print("*\t",end="")		#print "*\t",	# here , comma is use to avoid new line
		print("")					# here print is use to print new line
		
patter(4)