'''
Decorator demo
'''

'''
##
## 1) Functions inside Functions
##

# The outer function-f is called “Enclosed function” and the inner function-g is called “Nested function. 
def f():
	def g():
		print("Hi, its function g")
		print("thanks for calling")
		
	print("Hi, its function f")
	print("Now calling function g")
	g()
f()	
'''

'''	
##
## 2) Functions as Parameters
##
def foo():
	print("Hi, this is function foo")
	print("thanks for calling")
	
def caller(fun_name):
	print("I am caller function")
	print("Now calling function foo")
	fun_name()
	print("real value of fun_name is "+ fun_name.__name__)

caller(foo)
'''

##
## 3) Functions returning  Functions
##

def tempareture(t):
	def celsius2fahrenheit():
		return 9 * t / 5 + 32
	
	#result = "its "+ str(celsius2fahrenheit(t))+" degree"
	return celsius2fahrenheit
	
t_20 = tempareture(20)
print("t_20 is nothing but "+t_20.__name__)
print("its "+ str(t_20())+" degree")








