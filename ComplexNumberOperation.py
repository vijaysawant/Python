

class Complex:
	def __init__(self):
		
	def __str__(self):
		print "Happy Diwali"
		return str(self.real)+"+"+str(self.imag)
		
i = 10
print i
c = Complex(10,20)
print c			# it internally calls print c.__str__()		