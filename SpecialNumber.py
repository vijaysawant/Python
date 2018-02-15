"""
Program to check given number is special number or not.
"""

def CheckSpecialNumber(Num):
	sum = 0
	facto = 0
	originalNum = Num
	while Num >= 1:
		facto = findFactorial(int(Num % 10))
		sum = sum + facto
		Num = Num / 10
	
	if originalNum == sum:
		return 1
	else:
		return 0
		
def findFactorial(Num):
	facto = 1
	while Num:
		facto = facto * Num
		Num -= 1
	return facto
	
if __name__ == "__main__":
	Num = input("Enter Number : ")
	if CheckSpecialNumber(Num):
		print "Special Number"
	else:
		print "Not a special Number"
		
