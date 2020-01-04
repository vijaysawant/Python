"""
	Base
   /	\
Der1	Der2
   \	/
	Child

"""


class Base(object):
	def __init__(self):
		print"Base Constructor"
		
	def foo(self):
		print "Base foo"
		
	def bar(self):
		print "Base bar"
		
class Der1(Base):
	def __init__(self):
		print "Der1 Constructor"
	
	def bar(self):
		print "Der1 bar"
	
class Der2(Base):
	def __init__(self):
		print "Der2 Constructor"
		
	def foo(self):
		print "Der2 foo"
		
class Child(Der1, Der2):
	def __init__(self):
		print "Child Constructor"

if __name__ == "__main__":
	c = Child()
	c.bar()
	c.foo()
	