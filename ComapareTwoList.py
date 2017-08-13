'''
Program to check elements of 2 lists are same or not
'''

def CompareList(l1,l2):
	l1.sort()
	l2.sort()
	i = 0
	'''
	use additional input checking condition
	if type(l1) != list and type(l2) != list:
	'''
	if len(l1) != len(l2):
		return 0
	else:
		while i < len(l1):
			if l1[i] == l2[i]:
				i += 1
				continue
			else:
				return 0

	return 1

if __name__ == "__main__":
	list1,list2 = input("Enter 2 list comma seperately : ")
	res = CompareList(list1,list2)
	if res == 1:
		print "Equals"
	else:
		print "Not Equals"