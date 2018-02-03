'''
Enter String : "aaabbbccdaa"
Output = a3b3c2d1a2
'''

def GenrateWordCount(input_str):
	i = 0
	count = 0
	result_str = ""
	# a a b b b c c d d a b b b	= 13 chars
	while i < len(input_str):
		char_to_check = input_str[i]
		count = 1
		while (i+1 < len(input_str) and char_to_check == input_str[i+1]):
			count += 1
			i += 1
		result_str = result_str + char_to_check + str(count)
		i += 1
		
	return result_str
	
if __name__ == "__main__":
	input_str = input("Enter String : ")
	print GenrateWordCount(input_str)