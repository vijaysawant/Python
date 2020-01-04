"""
WaP to implement bank account, bank account should have following details
AccNum, HolderName, Address, Balance
"""
class BankAccount:

#class variable for account no and will be common to all object of BankAccount class
	Account_No_Generator = 1	# this is static variable i.e class variable in python (not instance variable)
	
#constructor and destructor
	def __init__(self,name,address,balance = 0):
		self.__HolderName = name
		self.__Address = address
		self.__Balance = balance
		self.__AccNum = BankAccount.Account_No_Generator
		BankAccount.Account_No_Generator += 1				# auto generation technique
			
	
	def WithDraw(self,amount):
		if(self.__Balance > amount):
			self.__Balance -= amount
			return True
		return False
	
	def Deposit(self,amount):
		if amount < 0:
			print "Amount should positive"
			return False
		else:
			self.__Balance += amount
			return True
			
#Getter method	
	def __GetAccNum(self):
		return self.__AccNum
		
	def __GetHolderName(self):
		return self.__HolderName
	
	def __GetAddress(self):
		return self.__Address
	
	def __GetBalance(self):
		return self.__Balance

	
if __name__ == "__main__":
	vijay = BankAccount("vijay","Bhor")
	print "Name :",vijay._BankAccount__HolderName
	print "Address :",vijay._BankAccount__Address
	print "Balance :",vijay._BankAccount__Balance
	print "Account :",vijay._BankAccount__AccNum
	
	vijay.Deposit(5000)
	print "After Depoit Balance = ",vijay._BankAccount__GetBalance()
	vijay.WithDraw(2000)
	print "After withdraw Balance = ",vijay._BankAccount__GetBalance()