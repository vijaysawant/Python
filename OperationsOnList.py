'''
	Program to perform operations on 2 Lists
'''
def IntersectionOfLists(L1, L2):
	resList = []
	if (type(L1) and type(L2) == list):
		for x in L1:
			if x in L2:
				resList.append(x)
	return resList

def UnionOfLists(L1, L2):
	resList = []
	i = 0
	j = 0
	if(type(L1) and type(L2) == list):
		while i < len(L1):
			j = 0
			while j < len(L2):
				if (L1[i] == L2[j] and L1[i] not in resList):
					resList.append(L1[i])
				if (L1[i] != L2[j]):
					if(L1[i] not in resList):
						resList.append(L1[i])
					if(L2[j] not in resList):
						resList.append(L2[j])
				j += 1
			i += 1
			
	return resList

def DifferenceOfSets(L1, L2):
	resList = []
	if (type(L1) and type(L2) == list):
		for x in L1:
			if x not in L2:
				resList.append(x)
	return resList
	
# Symmetric Difference or Inverse Intersection
def SymmetricDifference(L1, L2):
	resList = []
	if (type(L1) and type(L2) == list):
		for x in L1:
			if x not in L2:
				resList.append(x)
		for y in L2:
			if y not in L1:
				resList.append(y)
	return resList
	
if __name__ == "__main__":
	L1 = eval(input("Enter List1 Elements : "))
	L2 = eval(input("Enter List2 Elements : "))
	
	print("\nIntersection : ",IntersectionOfLists(L1, L2))
	print("Union : ",UnionOfLists(L1, L2))
	print("Difference : ",DifferenceOfSets(L1, L2))
	print("Symmetric Difference : ",SymmetricDifference(L1, L2))
	
'''
Output - 
	Enter List1 Elements : [1,2,3,4]
	Enter List2 Elements : [3,4,5,6]

	Intersection :  [3, 4]
	Union :  [1, 3, 4, 5, 6, 2]
	Difference :  [1, 2]
	Symmetric Difference :  [1, 2, 5, 6]
'''
	
	
	
	