"""
Check given number is power of 2's or not.
ex - 1,2,4,8,16,32 are power of 2's
"""
def Check2sPower(Num):
	if Num == 0:
		return 0
	cnt = 0
	m = 1
	while m <= Num:
		if Num & m == m:
			cnt += 1
		m = m << 1
	print "Num of 1's : ",cnt
	if cnt == 1:
		return 1
	else:
		return 0
		
"""
or simple solution
"""
def Check2sPower_or_not(num):
	return num != 0 and (num & (num-1) == 0)
		

if __name__ == "__main__":
	Num = input("Enter Number : ")
	if Check2sPower_or_not(Num):
		print "Yes {0} is power of 2's".format(Num)
	else:
		print "No {0} is not power of 2's".format(Num)