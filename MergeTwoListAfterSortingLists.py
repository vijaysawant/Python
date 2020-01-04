'''
Merge Sort - WAP to merge two lists in sorted way

input - list1 = [2,7,11,21] list = [1,3,4,5]
output - list = [1,2,3,4,5,7,11,21]	
'''

def MergeList(list1,list2):
	list1.sort()
	list2.sort()
	list = []
	i = 0
	j = 0
	
	while i < len(list1) and j < len(list2):
		if list1[i] < list2[j]:
			list.append(list1[i])
			i += 1
		else:	#list1[i] > list2[j]
			list.append(list2[j])
			j += 1
			
	if i < len(list1):
		list.extend(list1[i:])
	if j < len(list2):
		list.extend(list2[j:])
	return list

if __name__ == "__main__":
	list1, list2 = input("Enter elements for two Lists comma seperately: ")
	list = MergeList(list1,list2)
	print list
