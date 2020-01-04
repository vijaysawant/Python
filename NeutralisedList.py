'''
input = [1,2,[3,4,[5,6],7],8,[9,10],11]
output = [1,2,3,4,5,6,7,8,9,10,11]
'''
'''
def NeutralisedList(L1):
	i = 0
	L2 = []
	while (i < len(L1)):
		if type(L1[i]) != list:
			L2.append(L1[i])
		else:
			ExtendList(L2,L1[i])
		i += 1
	return L2
	
def ExtendList(L2,L3):		# Recursive call to same  
	j = 0
	while j < len(L3):
		if type(L3[j]) != list:
			L2.append(L3[j])
		else:
			ExtendList(L2,L3[j])
		j +=1
'''
L = []
def NeutralisedList(l1):
	i = 0
	while i < len(l1):
		if type(l1[i]) == list:
			NeutralisedList(l1[i])
		else:
			L.append(l1[i])
		i += 1
	return L


if __name__ == "__main__":
	list1= input("Enter list : ")
	List = NeutralisedList(list1)
	print List