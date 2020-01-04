'''
input - L1 = [1,2,3] L2 = [3,4,7,1]
output - [4,7,2]
'''


def InverseIntersection(L1,L2):
	L3 = []
	i = 0
	while i<len(L2):
		if L2[i] not in L1:
			L3.append(L2[i])
		else:
			L1.remove(L2[i])
		i+=1
		
	L3.extend(L1)
	return L3

if __name__ == "__main__":
	list1,list2 = input("Enter 2 lists, comma seperated : ")
	i_List = InverseIntersection(list1,list2)
	print i_List