"""
Write a simple BankAccount class. Account number
should be auto-generated. Implement withdraw, deposit and checkBalacne methods for the same.
Write a menu driven program to perform account operations.
"""

class BankAccount:
	AutoAccountNumber = 1
	def __init__(self, Name, Amt = 0):
		self.AccNum = BankAccount.AutoAccountNumber
		self.Name = Name
		self.Balance = Amt
		
		BankAccount.AutoAccountNumber += 1
		
	#def __del__(self):
	
	def Deposite(self, AutoAccountNumber, Amt):
		self.Balance = self.Balance + Amt
		
	def Withdraw(self, AutoAccountNumber, Amt):
		if self.Balance < Amt:
			print "Can not Withdraw..!!!"
		else:
			self.Balance = self.Balance - Amt
	
	def CheckBalance(self):
		return self.Balance
		
def Main():
	choice = 0
	print"select Operation\n1 Deposite\n2 Withdraw\n3 Check Balance\n4 Exit"
	choice = input("Enter Choice :")
	while 1:
		if choice == 1:
			Name = input("Enter Customer Name : ")
			Amt = input("Enter Amount to Deposite : ")
			obj = BankAccount(Name)
			obj.Deposite(obj.AccNum, Amt)
			print "Amount {0} Deposited to Account Num : {1}".format(Amt, obj.AccNum)
			break
		elif choice == 2:
			
			break
		elif choice == 4:
			break
		else:
			print "Wrong choice...!"
if __name__ == "__main__":
	Main()
	
	
	
	
	
	
	
	