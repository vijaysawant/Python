
def Occures(list,num):
	cnt = 0
	
	for i in range(len(list)):
		if list[i] == num:
			cnt += 1
	
	return cnt

list,num = input("Enter list elements and number to srch: ")
res = Occures(list,num)
print res