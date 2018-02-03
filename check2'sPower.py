
def check2sPower(Num):
	m = 1
	cnt = 0
	while m < Num:
		if Num & m == 1:
			cnt += 1
		m = m << 1
			

if __name__ == "__main__":
	num = input("Enter num : ")
	if (check2sPower(num)):
		print "True"
	else:
		print"False"
'''def Generic2sPowerDivisibilityTest(number,divisor):
	return (number & (divisor - 1))==0
	
if __name__ == "__main__":
	num, div = input("Enter num and divisor comma seperatly : ")
	if Generic2sPowerDivisibilityTest(num,div):
		print "True number is divisible divisor"
	else:
		print "False number is not divisible divisor"
'''