#
#	program to accept lower and upper bound and print
#	sum of even and sum of odd nums for given range
#

#! C:\Python\python

lower,upper = input("Enter start and end for number range : ")

Sum_Even = 0
Sum_Odd = 0

iCnt = lower
iEndCnt = upper


for iCnt in range(iEndCnt+1):
	if iCnt%2 == 0:
		Sum_Even += iCnt
		iCnt += 1
	else:
		Sum_Odd += iCnt
		iCnt += 1

print"Range of Nums = %d : %d"%(lower,upper)
print"Sum of Even Nums = %d"%(Sum_Even)
print"Sum of Odd Nums = %d"%(Sum_Odd)