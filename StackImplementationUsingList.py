list = []
top = -1
size = 10

def IsStackFull(l1):
	if len(l1) == 5:
		return 1
	else:
		return 0
		
def IsStackEmpty(l1):
	if len(l1) == 0:
		return 1
	else:
		return 0
		
def Push(l1,data):
	if IsStackFull(l1):
		print "Stack is Full\n"
		return 0
	else:
		l1.append(data)

def Pop(l1):
	if IsStackEmpty(l1):
		print "Satck is Empty\n"
		return 0
	else:
		data = l1.pop()
		return data

		
if __name__ == "__main__":
	l1 = []
	no = input("Enter num to push : ")
	Push(l1,no)
	print l1
	pop_res = Pop(l1)
	print pop_res