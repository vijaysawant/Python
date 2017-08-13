#
# Program to demonstrate concept of Default Arguments of user defined function
#

#! C:\Python\python.exe

#def Add(a,b = 20,c):
# SyntaxError "non-default argument follows default argument"
# Default arguments should be trailing

def Add(a,b = 20):
	print "a=%d b=%d"%(a,b)
	return a+b
	
def sub(c,d=10):
	print "c=%d d=%d"%(c,d)
	return c-d
	
	
'''	
res = Add(10)
print "Addition = %d"%res	# 30

res = Add(b = 2,a = 1)
print "Addition = %d"%res	# 3
'''
res = Add(12,b=1)
print "Addition = %d"%res	# 13

res = sub(10,5)
print "Substraction = %d"%(res)	# 5