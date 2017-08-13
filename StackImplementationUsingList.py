list = []
top = -1
size = 10

def IsStackFull(l1):
	global top
	global size
	if top == size-1:
		print "Full"
		return 0
	else:
		return 1
		
def IsStackEmpty():
	global top
	global size
	if top == -1:
		print "Empty"
		return 0
	else:
		return 1
		
def Push(l1,data):
	global top
	#global list
	if IsStackFull(l1):
		return 0
	else:
		top += 1
		l1[top] = data

def Pop(l1):
	global top
	#global list
	data = 0
	if IsStackEmpty():
		return 0
	else:
		data = l1[top]
		top -= 1
	return data
		
l1 = []
no = input("Enter num to push : ")
Push(l1,no)
print l1
#pop_res = Pop(l1)
#print pop_res