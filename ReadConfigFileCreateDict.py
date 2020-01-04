'''
program will take server.conf file as input file then parse that file and create dictiory
'''

def ParseConfigFile(FileName):
	result = {}
	section_details = {}
	section_name = " "		# for SERVER-1 and SERVER-2
	section_found = False

	fd = open(FileName)
	
	if fd != None:
		lines = fd.readlines()
		
		for line in lines:
			# avoid line starts with comments
			if line.startswith("#"):	#if line[0] == "#":
				continue
				
			if line.startswith("["):
				if section_found == True:
					result[section_name] = section_details
					section_found = False
					
				if section_found == False:
					section_name = line[1:-2]
					section_found = True
					section_details = {}
					
			elif section_found == True:
				config_line = line.split("=")
				if "#" in config_line[1]:
					config_line[1] = config_line[1].split("#")[0]
				section_details[config_line[0]] = config_line[1]
		else:
			result[section_name] = section_details
				
	return result


def main():
	file_name = input("Enter config file name:")
	result = ParseConfigFile(file_name)
	print result
	
if __name__=="__main__":
	main()