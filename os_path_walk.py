import os
import sys

c_count = 0
cpp_count = 0
py_count = 0
h_count = 0
other_count = 0
txt_count = 0
def callback(arg, directory, files):
	global c_count
	global cpp_count
	global py_count
	global h_count
	global other_count
	global txt_count
	for file1 in files:
		#print os.path.join(directory, file1)#, repr(arg)
		if file1.endswith(".py"):
			py_count += 1
		elif file1.endswith(".c"):
			c_count += 1
		elif file1.endswith(".cpp"):
			cpp_count += 1
		elif file1.endswith(".h"):
			h_count += 1
		elif file1.endswith(".txt"):
			txt_count += 1
		else:
			other_count += 1

def main():
    print sys.argv
    os.path.walk("D:\\", callback, "directory traverse")
    print "Python :", py_count, "C:",c_count,"CPP:", cpp_count,"header:", h_count,"txt:", txt_count, "others:",other_count

if __name__ == "__main__":
    main()
