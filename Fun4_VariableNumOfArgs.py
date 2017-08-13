#
# Program to demonstrate concept of Variable Number of Arguments of user defined function
#

#! C:\Python\python.exe

def fun(* var):
	print(type(var))
	for x in var:
		print x

fun(1,2,3)			# passing numbers as arguments
fun(["a","abc",3],5)# passing list and a number as arguments

''' 
Output-

<type 'tuple'>
1
2
3

<type 'tuple'>
['a', 'abc', 3]
5
'''
#
# Variable number of arguments contain * in function argument list
#