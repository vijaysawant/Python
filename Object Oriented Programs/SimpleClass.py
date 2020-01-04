
class SimpleClass:
	# Class Attribute
	institute_name = "Trinaha solutions\n"
	
	def __init__(self, value):
		# Object Attribute
		self.object_attribute = value
		self.__private_attribute = 100
		print "Constructor"
		
	def __del__(self):
		print "Destructor"
		
	def setAttribute(self, value):
		self.object_attribute = value
		
	def getAttribute(self):
#		print "ID :",id(self)
		return self.object_attribute
	
	def __setPrivateAttribute(self, value):
		self.__private_attribute = value
	
		
if __name__ == "__main__":
	x = SimpleClass(10)	
	y = SimpleClass(20)
	
	print x.getAttribute()
	print y.getAttribute()
	
	print SimpleClass.institute_name
	x.teach = True	# now create object attribute in this way also
	
	print x.__dict__
	print y.__dict__
	print SimpleClass.__dict__

	print "Private Member :",x._SimpleClass__private_attribute
	x._SimpleClass__setPrivateAttribute("ABC")
	print "Private Member :",x._SimpleClass__private_attribute