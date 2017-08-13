# ListAndTouple.txt File containing Book information and 
# lines of the form "Bookname,SerialNum,price"

FileName = "ListAndToupleInput.txt"
BookInfo = []			# Empty list of book information
for line in open(FileName):
	FileRow = line.split(",")		# Split each line into a list
	
	BookName = FileRow[0]			# Extract and convert individual fields
	SerialNum = int(FileRow[0][1])
	price = float(FileRow[0][2])
	
	BookDetails = (BookName,SerialNum,price)	# Create a touple (BookName,SerialNum,price)
	BookInfo.append(BookDetails)				# Append to list of records