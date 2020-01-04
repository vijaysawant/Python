'''
WAP to accept 2 strings from user and check if second string is rotation of
first or not
ex -
	input - "watermelon","lonwaterme"
	output- True
'''
def StrRotation(str,chk_str):
	if len(str) != len(chk_str):
		print "Length of input string and chk_str not match"
		return False
	if chk_str in str+str:
		return 1
	else:
		return 0

if __name__ == "__main__":
	res = 0
	str,chk_str = input("enter str and sub string : ")
	if StrRotation(str,chk_str):
		print ("{} is Rotation of {}".format(chk_str,str))
	else:
		print ("{} is NOT Rotation of {}".format(chk_str,str))
	