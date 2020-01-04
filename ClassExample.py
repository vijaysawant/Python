class Test:
	m_iClassAttribute = 0
	
	def __init__(self):
		print "Constructor"
		self.m_iClassAttribute = 0
		
	def __del__(self):
		print "Destructor"
		
	def SetI(self,i):
		print "Setter method"
		self.m_iClassAttribute = i
	
	def GetI(self):
		print "Getter method"
		return self.m_iClassAttribute
		
if __name__ == "__main__":
	print "Creating object"
	t = Test()
	#t.bhairavi()
	t.SetI(15)
	print t.GetI()
	