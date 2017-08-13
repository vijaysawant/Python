#
#	Program to cheak date is valid or not
#

#! C:\Python\python.exe

print"Enter DD in between 1 to 31\n\
	\rEnter MM in between 1 to 12\n\
	\rEnter YY in between 2000 to 2100\n"
d,m,y = input("Enter DD,MM,YYYY Comma Seperately : ")
flag = 1
if d>0 and d<32:
	if m>0 and m<13:
		if y>2000 and y<2100:
			print"\nDate saved.."
		else:
			flag = 0
			print"\nYY is not proper"
	else:
		flag = 0
		print"\nMM is not proper"
else:
	flag = 0
	print"\nDD is not proper"

if flag == 1:
	print"\nDate in various format:"
	print"DD:MM:YY : {}:{}:{}".format(d,m,y)
	print"MM:DD:YY : {1}:{0}:{2}".format(d,m,y)
	print"YY:MM:DD : {2}:{1}:{0}".format(d,m,y)
