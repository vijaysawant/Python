

class Stack:
	
	def __init__(self, stackSize = 5):
		self.STACK = []
		self.size = stackSize

		
		
	def __del__(self):
		del self.STACK
		
	def Push(self, data):
		self.STACK.append(data)
		
	def Pop(self):
		return self.STACK.pop()
		
	def IsFull(self):
		return len(self.STACK) == self.size
		
	def IsEmpty(self):
		return self.STACK == []

def UsageMenu():
	print "1 PUSH\n2 POP\n3 Exit"
	return intput("Enter choice :")
	
def Main():
	userChoice = 0
	studentCnt = input("Number of students : ")
	student = Stack(studentCnt)
	print"Operations on Student Stack :"
	userChoice = UsageMenu()
	while 1:
		# PUSH activity
		if userChoice == 1:
			if student.IsFull():
				print "Stack is Full..!!!"
				return
			else:
				data = input("Enter Student Name :")
				student.Push(data)
				continue
		# POP activity
		elif userChoice == 2:
		
		
		elif userChoice == 3:
			return 1
		else:
			print "Enter valid choice"
			UsageMenu()
	
if __name__ == "__main__":
	Main()