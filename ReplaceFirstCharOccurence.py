"""
WAP to accept string and replacing charactor, which replaces all other occurences of
first charactor of that string
(in our case first char of string is t and replacing char is *)
ex - 
	input - "that is the best thing","*"
	outpuy- "tha* is *he bes* *hing"
"""

def ReplaceFirstCharOccurence(input_str,replace_by):
	return input_str[0] + input_str[1:].replace(input_str[0],replace_by)
	

if __name__=="__main__":
	str,replace = input("Enter string and replace char, comma seperated :")
	print ReplaceFirstCharOccurence(str,replace)
