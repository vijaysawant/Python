"""
Copy source file content into destination file and argument should be command line argument
copyFile_cmdLine.py <src_file> <dest_file>
"""

import argparse
import shutil


def MyCopyFile(src_File, dest_File, num_of_Lines):
	src_fd = open(src_File, "r")
	dest_fd = open(dest_File, "w")
	
	if num_of_Lines == 0:
		# copy all lines from src file to dest file
		shutil.copyfileobj(src_fd, dest_fd)
	else:
		line = src_fd.readline()
		while line != "" and num_of_Lines != 0:
			dest_fd.write(line)
			line = src_fd.readline()
			num_of_Lines -= 1
	
	src_fd.close()
	dest_fd.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	
	parser.add_argument("-s", type = str, help = "Source File Name")
	parser.add_argument("-d", type = str, help = "Destination File Name")
	parser.add_argument("-n", type = int, help = "Number of lines to copy", default = 0)
	args = parser.parse_args()
	
	print "Source File : ",args.s, "Destination File : ",args.d
	print "Number of lines to copy : ",args.n
	
	MyCopyFile(args.s, args.d, args.n)