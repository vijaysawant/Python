"""
Program to create archive file of specific location / path
"""

import shutil

def MakeArchive(path, RootDir):
	archive_name = shutil.make_archive(path, "zip")
	print "Archive Name : ",archive_name


if __name__ == "__main__":
	path = input("Enter path to create Archive : ") # all files from this location will get be archive
	RootDir = input("Enter Root Directory : ")
	MakeArchive(path, RootDir)
	
	
	
"""
Output - 
	Enter path to create Archive : "D:\Git_Workplace\python"
	Enter Root Directory : "D:\Python Programs"
	Archive Name : D:\Git_Workplace\python.zip
	
"""