""" 
Program to accept 2 Unsorted Lists from user, sort them and merge them into single List
"""
# selection sort
def SortList(anyList):
	#				i = [0,1,2,3]
	for i in range(len(anyList)):
	#				j = [1,2,3]
		for j in range (i+1, len(anyList)):
			if anyList[i] > anyList[j]:
				temp = anyList[i]
				anyList[i] = anyList[j]
				anyList[j] = temp
				
	return anyList

def MergeList(l1,l2):
	ResultList = []
	i = j = 0
	while i < len(l1) and j < len(l2):
		if l1[i] < l2[j]:
			ResultList.append(l1[i])
			i += 1
		else:
			ResultList.append(l2[j])
			j += 1
			
	if i == len(l1):
		ResultList.extend(l2[j:])
	else:
		ResultList.extend(l1[i:])
		
	return ResultList


if __name__ == "__main__":
	myList1 = [8,5,3,6]			# input("Enter List Elements in [ ] : ")
	myList2 = [4,7,9,1,2,3.5]	# input("Enter List Elements in [ ] : ")
	
	print "List1 : ",myList1,"List2 : ",myList2
	
	print "After sort : "
	print "List1 : ",SortList(myList1),"List2 : ",SortList(myList2)
	
	print "After Merging : ",MergeList(myList1,myList2)
