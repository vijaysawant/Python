#
# Program to demonstrate concept of Positional Arguments of user defined function
#

#! C:\Python\python.exe

def Add(a,b):
	print "a=%d b=%d"%(a,b)
	return a + b

res = Add(10,20)
print "Addition = %d"%res

# function that taking list as argument
def myfun(list):
	return list[0]+list[1]+list[2]
	
res = myfun([1,2,3])
print res

#
# Here 10 and 20 are positional arguments because
# after resolving function a is 10 and b is 20
#