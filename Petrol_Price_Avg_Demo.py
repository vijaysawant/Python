"""
Program to read petrol prices from file and find out average petrol price from different states
file contains data like below format
	YEAR MH KN GA
	
Jan 2017 80 81 70
Feb 2017 81 82 71
Mar 2017 79 78 68
"""


def Calculat_Avg_Price(file_Name):
	file_fd = open(file_Name, "r")
	MH_Price = 0
	KN_Price = 0
	GA_Price = 0
	cnt_months = 0
	
	line = file_fd.readline()
	while line != "":
		data = line.split(" ")
		MH_Price = MH_Price + int(data[2])
		KN_Price = KN_Price + int(data[3])
		GA_Price = GA_Price + int(data[4])
		cnt_months += 1
		line = file_fd.readline()
	
	print "Avg Price, MH in 2017 : ",(MH_Price/cnt_months)
	print "Avg Price, KN in 2017 : ",(KN_Price/cnt_months)
	print "Avg Price, GA in 2017 : ",(GA_Price/cnt_months)
	file_fd.close()
	
if __name__ == "__main__":
	FileName = input("Enter file name : ")
	Calculat_Avg_Price(FileName)