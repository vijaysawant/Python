# Global variable, for key of EMP_DICT
emp_id = 0

def SearchRecord(Dict_to_Srch, name):
	if len(Dict_to_Srch) == 0:
		print "No Record available"
		return None
	values = Dict_to_Srch.itervalues()
	# values is of type = <type 'dictionary-valueiterator'>
	
	for sub_dict in values:
		for key in sub_dict:
			if sub_dict["Name"] == name:
				print "Record Found"
				print "Name = ",sub_dict["Name"], "Address = ",sub_dict["Addr"], "Salary = ",sub_dict["Salary"]
				return True
			else:
				print name,"Record Not Found\n"
				return False


def EmpRecord(name, addr, sal):
	emp = {}
	emp["Name"] = name
	emp["Addr"] = addr
	emp["Salary"] = sal
	return emp
	
def insertRecord(Dict_to_insert, name, addr, sal):
	global emp_id
	emp_id += 1
	res_Dict = EmpRecord(name, addr, sal)
	Dict_to_insert[emp_id] = res_Dict

def Display_Dict(Dict_to_Print):
	for key in Dict_to_Print:
		print key, Dict_to_Print[key]
	
	
def Menus():
	print "\n1. Insert Record\n2. Remove Record\n3. Search Record\n4. Modify Record\n5. Disply\n6. Exit"
	choice = input("Enter Your Choice : ")
	return choice
	
if __name__ == "__main__":
	choice = Menus()
	EMP_DICT = {}

	while 1:
		if choice == 1:
			cnt = 0
			cnt = input("\nHow many records you want to insert : ")
			while cnt != 0:
				name, addr, sal = input("Enter Name, Addr, Sal : ")
				insertRecord(EMP_DICT, name, addr, sal)
				cnt -= 1
			else:
				print EMP_DICT
				choice = Menus()
		if choice == 2:
			pass
			
		if choice == 3:
			name = input("Enter name to Search : ")
			SearchRecord(EMP_DICT, name)
			choice = Menus()
		
		if choice == 5:
			Display_Dict(EMP_DICT)
			choice = Menus()
			
		if choice == 6:
			break