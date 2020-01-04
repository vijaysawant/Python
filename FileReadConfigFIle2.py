def ReadConfigFile(file_name):
	fd = open(file_name)
	res = {}
	line = fd.readline()
	
	while line != "":
		if line.startswith("["):
			ReadConfigFile(line)
		if not line.startswith("#"):
			if "=" in line:
				l1 = line.split("=")
				value = l1[1]
				if "#" in l1[1]:
					value = l1[1].split("#")[0]
				res[l1[0]] = value
		line = fd.readline()
	return res

def ReadSection(line):
	retVal = line
	print retVal
if __name__ == "__main__":
	fileName = input("Enter File name : ")
	config_Dict = ReadConfigFile(fileName)
	print config_Dict