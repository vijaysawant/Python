#
#	Program to cheak time is valid or not
#

#! C:\Python\python.exe

print"Enter Hrs in between 0 to 24\n\
	\rEnter Min in between 0 to 60\n\
	\rEnter Sec in between 0 to 60\n"
h,m,s = input("Enter DD,MM,YYYY Comma Seperately : ")
flag = 1

if h>=0 & h<=12:
	if m>=0 & m<=60:
		if s>=0 & s<=60:
			print"Valid Time\n"
		else:
			flag = 0
			print"Sec should be proper"
	else:
		flag = 0
		print"min should be proper"
else:
	flag = 0
	print"hrs should be proper"
	
if flag == 1:
	if h <= 12:
		print("Time : {}:{}:{} AM".format(h,m,s))
	else:
		print("Time : {}:{}:{} PM".format(h,m,s))