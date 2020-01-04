import re


def main():
	in_regex = input("Enter regex object :")
	IN_REG_EX_OBJ = re.compile(in_regex)
	for i in range(1,6):
		in_str = input("Enter Input string %d:"%i)
		#print IN_REG_EX_OBJ.search(in_str)
		for match in IN_REG_EX_OBJ.finditer(in_str):
			print (match.start(),match.end())		# it prints start and end of match index
	
if __name__ == "__main__":
	main()