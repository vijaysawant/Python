
def MaxMin(list):
	max = list[0]
	min = list[0]
	i = 0
	while i < len(list):
		if(list[i] > max):
			max = list[i]
		if(list[i] < min):
			min = list[i]
		i += 1
	return max,min	
			
list = input("Enter list : ")
res1,res2 = MaxMin(list)
print res1,res2