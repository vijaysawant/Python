'''
Program to accept two lists from user and return the Intersection of them
(i.e return a list which contains commom elements from them)
ex-
	list1 = [2,3,5,8,1,9,1] list2 = [2,4,5,1,7,8,9]
	intersection = [2,5,8,1,9,1]
	Union 		 = [2,3,5,8,1,9]
	inverse intersection = [3]

'''
def ListIntersection(L1,L2):
	#L1.sort()
	#L2.sort()
	if len(L1) == 0 or len(L2) == 0:
		return []
	L = []
	for i in range(len(L1)):
		for j in range(len(L2)):
			if L1[i] == L2[j]:
				L.append(L1[i])
			else:
				pass
				
	return L



if __name__ == "__main__":
	list1,list2 = input("Enter 2 lists, comma seperated : ")
	i_List = ListIntersection(list1,list2)
	print i_List