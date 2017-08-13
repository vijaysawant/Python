#
# Program to demonstrate concept of Keyword Arguments of user defined function
#

#! C:\Python\python.exe

def Add(a,b,c = 20):
	print "a=%d b=%d c=%d"%(a,b,c)
	return a+b+c

res = Add(10,b = 5,c = 10)
print "Addition = %d"%res	# 25

# res = Add(10,b = 5,0)
# SyntaxError "non-keyword arg after keyword arg"