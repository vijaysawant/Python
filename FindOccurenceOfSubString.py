'''
input = "india"  sub_str = "i"
output = 2
'''
# use find() method which return lowest index of substring
def StringOccurence(input_string,sub_str):
	cnt = 0
	i = 0
	while i < len(
	
	return cnt


'''	# this is for checking charector by charactor
def StringOccurence(input_string,sub_str):
	i = 0
	cnt = 0
	while i < len(input_string):
		if input_string[i] == sub_str:
			cnt += 1
		i+=1
	return cnt
'''
	
if __name__ == "__main__":
	cnt = 0
	input_string,sub_str = input("Enter stirng and substring to find occurence : ")
	cnt = StringOccurence(input_string,sub_str)
	print cnt