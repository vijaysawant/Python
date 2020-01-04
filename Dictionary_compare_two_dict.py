'''
Program to compare two dictionaries, key and value wise and return TRUE or FALSE
'''
def compare_dict(d1,d2):
	
	RetValue = True
	
	# check type of both dictionary
	if type(d1) != dict or type(d2) != dict:
		print "Type is not dictionary"
		RetValue = False
		
	# check length of both dictionary
	elif len(d1) != len(d2):
		print "length of dictionary not same"
		RetValue =  False
	else:
		for key in d1:
			if key in d2 and d1[key] == d2[key]:
				continue
			RetValue = False
			break
	return RetValue
	
def main():
	d1,d2 = input("Enter 2 Dictionaries comma seperately : ")
	if compare_dict(d1,d2):
		print "Both dictionary are same"
	else:
		print "Not same"
if __name__ == "__main__":
	main()