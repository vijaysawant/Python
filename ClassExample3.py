'''
program to demonstrate concept of class access variable 
'''

class Test:
	def __init__(self):
		self.iPublic = 100			# public member of class
		self.__iPrivate = 1000		# private member of class
		
	def get_private(self):
		return self.__iPrivate
		
	def set_private(self,data):
		self.__iPrivate = data
		
	def __PrivateFunction(self):
		print("called private function")
		
	def display(self):
		self.__PrivateFunction()
		
def main():
		t1 = Test()
		t1.iPublic = 1100
		print(t1.iPublic,t1.get_private())
		t1.__iPrivate = 1500
		#print "dictonary:",t1.__dict__
		#print t1._Test__iPrivate
		t1.display()
		''' To access private functions of class use syntax
		Obj._classnameVarName		- Here VarName is Private Variable
		#t1._Test__PrivateFunction()	
		#t1._Test__iPrivate
		'''
if __name__=="__main__":
	main()