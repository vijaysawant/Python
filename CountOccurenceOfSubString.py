'''
WAP to accept 2 strings from user, input string and sub string and 
count the occurence of sub string in input string
ex - 
	input = "that is the pthon book","th" 
	output = "th" Occures in "that is the pthon book" 3 times
'''
# use find() method which return lowest index of substring
def StringOccurence(input_string,sub_str):
	cnt = 0
	i = 0
	while i < len(input_string):
		if sub_str in input_string:
			cnt += 1
			i = input_string.find(sub_str)
			input_string = input_string[i+1:]
		i+=1
	return cnt
	
if __name__ == "__main__":
	cnt = 0
	input_string,sub_str = input("Enter stirng and substring to find occurence : ")
	cnt = StringOccurence(input_string,sub_str)
	print ("\"{}\" Occures in \"{}\" {} times").format(sub_str,input_string,cnt)
	
	
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