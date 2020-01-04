class Human:
	def __init__(self,name,addr):
		self.Name = name
		self.Address = addr
		
	def __del__(self):
		print"destructor"
		
	
if __name__ == "__main__":
	h1 = Human("vijay","Bhor")
	print h1.Name
	print h1.Address
	
	h2 = Human("jeetendra","pune")
	h2.teach = True
	print h2.Name
	print h2.Address
	print h2.teach