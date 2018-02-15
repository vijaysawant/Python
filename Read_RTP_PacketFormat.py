
def Create_RTP_Format(ver, padding, extension, cc, marker, pt, sequenceNum):
	packet = ver
	
	packet = packet << 1	# make 1 bit space for padding bit
	packet = packet | padding & ((1 << 1)-1 )
	
	packet = packet << 1	# make 1 bit space for extension bit
	packet = packet | extension & ((1 << 1)-1 )
	
	packet = packet << 4	# make 4 bits space for CSRC count bit
	packet = packet | cc & ( (1 << 4)-1 )
	
	packet = packet << 1	# make 1 bit space for marker bit
	packet = packet | marker & ( (1 << 1)-1 )
	
	packet = packet << 7	# make 7 bits space for payload type bit
	packet = packet | pt & ( (1 << 7)-1 )
	
	packet = packet << 16	# make 7 bit space for Sequence Number bit
	packet = packet | sequenceNum & ( (1 << 16)-1 )
	
	return packet

def Depacetise_RTP_Format(packet):
	sequenceNum = packet & ((1 << 16) - 1)
	packet = packet >> 16
	
	pt = packet & ((1 << 7)-1)
	packet = packet >> 7
	
	marker = packet & ((1 << 1)-1)
	packet = packet >> 1
	
	cc = packet & ((1 << 4)-1)
	packet = packet >> 4
	
	extension = packet & ((1 << 1)-1)
	packet = packet >> 1
	
	padding = packet & ((1 << 1)-1)
	packet = packet >> 1
	
	ver = packet & ((1 << 2)-1)
	
	print ver, padding, extension, cc, marker, pt, sequenceNum

	
	
	
if __name__ == "__main__":
	print "Enter RTP Format Data"
	ver = input("2 bits Protocol VERSION : ")
	padding = input("1 bit PADDING value : ")
	extension = input("1 bit presence of EXTENSION Header : ")
	cc = input("4 bits CSRC identifiers : ")
	marker = input("1 bit MARKER bit : ")
	pt = input("7 bits PAYLOAD TYPE : ")
	sequenceNum = input("16 bits SEQUENCE NUMBER : ")
	
	packetData = Create_RTP_Format(ver, padding, extension, cc, marker, pt, sequenceNum)
	print "packet Data : ",packetData
	print "Now depacketise packet Data : "
	Depacetise_RTP_Format(packetData)
	
'''	
bit positions -	‭10 1 1 1000 1 1000110 0111000000000000‬
Enter RTP Format Data
2 bits Protocol VERSION : 2
1 bit PADDING value : 1
1 bit presence of EXTENSION Header : 1
4 bits CSRC identifiers : 8
1 bit MARKER bit : 1
7 bits PAYLOAD TYPE : 70
16 bits SEQUENCE NUMBER : 28672

packet Data : 3100012544
	
'''