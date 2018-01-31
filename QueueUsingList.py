"""
Program to impliment Queue Data structure using List
"""
MaxSize = 5

def Enqueue(anyList, data):
	if IsQueueFull(anyList):
		print("Queue is Full\n")
	else:
		myList.append(data)
		
def Dequeue(anyList):
	if IsQueueEmpty(anyList):
		print("Queue is Empty\n")
	else:
		DequeuedElement = anyList[0]
		anyList.remove(anyList[0])
		return DequeuedElement

def IsQueueFull(anyList):
	global MaxSize
	if len(anyList) == MaxSize:
		return 1
	else:
		return 0
		
def IsQueueEmpty(anyList):
	if len(anyList) == 0:
		return 1
	else:
		return 0

if __name__ == "__main__":
	myList = []
	element = eval(input("Enter Element : "))
	Enqueue(myList,11)
	Enqueue(myList,22)
	Enqueue(myList,33)
	Enqueue(myList,44)
	Enqueue(myList,55)
	Enqueue(myList,element)

	print ("Queue : ",myList)

	print ("Dequeue : ",Dequeue(myList))
	print ("Queue : ",myList)
