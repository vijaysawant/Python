'''
WAP to implement our own fromkeys() method
ex-
	>>> d = {"name":"vijay","age":23}
	>>> d
	{'age': 23, 'name': 'vijay'}

	>>> result = dict.fromkays(d,[24,"swapnil"])
	>>> result (default output)
	{'age': [24, 'swapnil'], 'name': [24, 'swapnil']}

	expect output is {'age':24, 'name':'swapnil'}
'''
import sys

def from_key(d,ValuesList = None):
	result = {}
	
	#verify d is dictionary or not
	if type(d) != dict:
		print "Enter input not a dictionary"
		sys.exit(0)
	
	#verify ValuesList is container or not
	if type(ValuesList) == list or type(ValuesList) == tuple:
		KeysLen = len(d.keys())	# find length of keys
		
		#for DictKey in d.keys():
		for key in d.keys():
			result.keys = key
			print key
	
	
	
	
def main():
	d = input("Enter Dictionary : ")
	valueLists = input("Enter valuesList : ")
	print from_key(d,valueLists)
if __name__ == "__main__":
	main()