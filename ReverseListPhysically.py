def ReverseList(list):
	length = len(list)
	i = 0-
	j = length-1		# length of original list - 1
	rev_list = []		# create empty list
	while i < length:
		rev_list.append(list[j])
		i += 1
		j -= 1
	
	return rev_list

if __name__ == "__main__":
	list = input("Enter elements of List : ")
	rev_list = ReverseList(list)
	print rev_list
