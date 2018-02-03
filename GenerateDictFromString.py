'''
aaabbbccdaa
a3b3c2d1a2
output - 
{
	a : 5
	b : 3
	c : 2
	d : 1
}
'''
def GenrateDictCount(input_str):
	i = 0
	result_dict = {}
	
	while i < len(input_str):
		if result_dict.has_key(input_str[i]):
			result_dict[input_str[i]] = result_dict[input_str[i]] + 1
		else:
			result_dict[input_str[i]] = 1	# here input_str[i] will assign as key in result_dict and value is 1
		i += 1
	return result_dict
	
if __name__ == "__main__":
	input_str = input("Enter String : ")
	print GenrateDictCount(input_str)