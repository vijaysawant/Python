
import os

dir_files = []
dir_files1 = []

def compare_dir(args, dir, files):
	
	#for file in files:
	args.extend(files)
	#print type(files)	
	

if __name__ == "__main__":
	global dir_files
	global dir_files1
	
	path1 = input("Enter path,1 : ")
	path2 = input("Enter path,2 : ")
	
	os.path.walk(path1, compare_dir, dir_files)
	os.path.walk(path1, compare_dir, dir_files1)
	
	if len(dir_files) == len(dir_files1):
		print "true"
	