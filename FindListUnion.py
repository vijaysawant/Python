'''
Program to find out union of 2 list (i.e only common elements once and all other)

	ex - L1 = [2,3,5,8,1,9,1] L2 = [2,4,5,1,7,8,9]
		Union = L = [2,3,5,8,1,9,4]
'''
def ListUnion(L1,L2):
	i = 0
	L = []
	L.append(L1[0])
	
	while i < len(L1):
		if L1[i] not in L:
			L.append(L1)
		i+=1
	
	i = 0
	while i < len(L2):
		if L2[i] not in L:
			L.append(L2)
		i+=1
	return L
'''
def ListUnion(L1,L2):
	#L1.sort()
	#L2.sort()
	if len(L1) == 0 or len(L2) == 0:
		return []
	L = []
	for i in range(len(L1)):
		for j in range(len(L2)):
		
			if L1[i] == L2[j]:
				for k in range(len(L)):
					if len(L) == 0:
						L.append(L1[i])
					if L1[i] == L[k]:
						pass
			else:
				L.append(L1[i])
				L.append(L2[j])	
	return L
'''
'''
# sir code
def ListUnion(L1,L2):
	L = L1; i = 0
	
	while i < len(L2):
		L.append(L2[i])
		i+=1
	return L
'''

if __name__ == "__main__":
	list1,list2 = input("Enter 2 lists, comma seperated : ")
	i_List = ListUnion(list1,list2)
	print i_List