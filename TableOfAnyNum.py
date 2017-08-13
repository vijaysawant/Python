#
#	program to accept accept range from user and display
#	sum of multiples of 6 (table of 6)
#

#! C:\Python\python

StartRange = input("Enter\nstart Range : ")
EndRange = input("End Range : ")

sum = 0
Start_Cnt = StartRange
End_Cnt = EndRange+1

for Start_Cnt in range(End_Cnt):
	if Start_Cnt % 6 == 0:
		sum += Start_Cnt
	Start_Cnt += 1
		
print"Sum of multiples of 6 in range %d to %d = %d"%(StartRange,EndRange,sum)