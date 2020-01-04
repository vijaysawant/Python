'''
Wap to accept srch pattern, replace pattern and input string in which 
the search pattern is to be search and replace by replace pattern
Hint - sub(), or subn()
'''

import re
"""
def RE_Srch_And_Replace(srch_pattern, replace_pattern, input_string):
	return re.sub(srch_pattern, replace_pattern, input_string)
	
def main():
	input_string = input("Enter input string :")
	srch_pattern = input("Enter search pattern :")
	replace_pattern = input("Enter replace pattern :")

	print RE_Srch_And_Replace(srch_pattern, replace_pattern, input_string)
	
if __name__ == "__main__":
	main()
	
	"""
import re

def RE_Srch_And_Replace(srch_pattern, replace_pattern, input_string,cnt):
	return re.sub(srch_pattern, replace_pattern, input_string,cnt)
	
def main():
	input_string = input("Enter input string :")
	srch_pattern = input("Enter search pattern :")
	replace_pattern = input("Enter replace pattern :")
	cnt = input("Enter replace count :")
	print RE_Srch_And_Replace(srch_pattern, replace_pattern, input_string,cnt)
	
if __name__ == "__main__":
	main()