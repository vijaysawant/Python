

def ListDemo(element):
	myList = [1,2,3,4,5]
	if type(element) == list:
		myList.extend(element)	# iterator should be extended
	else:
		myList.append(element)	# not iterator i.e. element should be append
	return myList
	
	
if __name__ == "__main__":
	element = input("Enter element or container to be inserted in list : ")
	res = ListDemo(element)
	print res