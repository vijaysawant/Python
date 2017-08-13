#
# Program to demonstrate concept of Variable Number of Arguments of user defined function
#

#! C:\Python\python.exe

def Fun(a,b,*var,**var1):
	print(type(a))
	print(type(b))
	print(type(var))
	print(type(var1))
	
	print a,b
	for n in var:
		print n
	
	for n in var1:
		print n,var1[n]
		
Fun(1,2,3,4,5,6,name="abc",sal="100000")

"""
Output :-

<type 'int'>
<type 'int'>
<type 'tuple'>
<type 'dict'>
1 2
3
4
5
6
name abc
sal 100000
"""