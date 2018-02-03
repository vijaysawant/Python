myList = []
MaxSize = 7


def PushElement(myStack, element):
	if len(myList) < MaxSize:
		myList.append(element)
	else:
		print "stack is already full\n"
		
def PopElement(myStack):
	if len(myList) == 0:
		print "stack is already empty\n"
		return 0
	else:
		return myList.pop()

def StackUsingList(choice):
	if choice == 1:
		element = input("Enter element : ")
		PushElement(myList, element)
		Main()
	if choice == 2:
		print "Poped : ",PopElement(myList)
		DisplayStack()
		Main()
	if choice == 3:
		DisplayStack()
		Main()

def DisplayStack():
	print "\nStart->",myList,"<-End\n"
	
def Main():
	choice = input("\n1.Push 2.Pop 3.Display 4.Exit\nEnter Choice : ")
	while choice != 4:
		StackUsingList(choice)
			

if __name__ =="__main__":
	Main()