"""
Program to accept file name and filter from user, based on that filter
output should be
1. if filter comes as empty then count total lines
2. if filter comes as ^string (ex - ^Hello) then line count should
   be lines "starts with Hello"
3. if filter comes as string$ (ex - Hello$) then line count should
   be lines "ends with Hello"
4. if filter comes as string (ex - Hello) then line count should be
   line "contains word Hello"
"""

def FilterToPrintLines(file, filter):
	if file == "":
		print "Enter file name"
		return -1
		
	fd = open(file)
	if "^" not in filter and "$" not in filter:
		ln = fd.readline()
		while ln:
			if filter in ln:
				print ln
			ln = fd.readline()
		return 1
	
	# starts with "^......"
	if filter.startswith("^"):
		ln = fd.readline()
		while ln:
			if ln.startswith(filter[1:]):
				print ln
			ln = fd.readline()
		return 1
		
	# ends with ".......$"
	# use strip to remove \n from string
	if filter.endswith("$"):
		ln = fd.readline()
		while ln:
			ln = ln.strip("\n")
			if ln.endswith( filter [ 0 : -1 ] ):
				print ln
			ln = fd.readline()
		return 1
		
	if filter == "" or filter == " ":
		count = 0
		ln = fd.readline()
		while ln:
			count += 1
			ln = fd.readline()
		else:
			print "Filter is Empty\nTotal Num of lines {0}".format(count)
			return 1
		
if __name__ == "__main__":
	fileName = filter = None
	print "Filter should be..\n1. string 2. ^string 3. string$ 4. \" \"(empty string)"
	fileName = input("Enter File name : ")
	filter = input("Enter Filter : ")
	FilterToPrintLines(fileName, filter)