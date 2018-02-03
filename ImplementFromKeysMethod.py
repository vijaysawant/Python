'''
def myFromKeys(anyDict, data):
	y = {}
	if type(data) == list or type(data) == tuple:
		for key in anyDict.keys():
			for val in data:
				y[key] = val
				
	else:
		y = dict.fromkeys(anyDict,data)
		
		
	return y
'''
def myFromKeys1(input_dict, output_dict_values):
	result_dict = {}
	if type(output_dict_values) == list or type(output_dict_values) == tuple:
		keys_list = input_dict.keys()
		values_length = len(output_dict_values)
		for i in range(len(keys_list)):
			if i < values_length:
				result_dict[keys_list[i]] = output_dict_values[i]
			else:
				result_dict[keys_list[i]] = None
	else:
		result_dict = dict.fromkeys(input_dict, output_dict_values)
	return result_dict

if __name__ == "__main__":
	myDict = input("ENter Input DIctionaly like {key:value,...} : ")
	values = input("Enter Output Values : ")
	print myFromKeys1(myDict, values)
	
	
