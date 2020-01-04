'''
Closure Demo
'''

def myDecorator(closure_value):
	print(f"2 : Closure Value : {closure_value}")
	def add(num):
		print(f"5 : Addition on {num} and {closure_value} will be returned")
		return num + closure_value
	print(f"3 : returning closure function name : {add}")
	return add
	
# here 10 in closure value to myDecorator function
print("1 : passing closure value to function")
add_10 = myDecorator(10)
print("4 : Call to closure function")
print(f"6 : Result : {add_10(5)}")