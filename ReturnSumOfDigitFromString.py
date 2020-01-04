def SumOfDigitsFromSting(input_str):
	i = 0
	sum = 0
	while i < len(input_str):
		if input_str[i].isdigit():
			sum = sum + int(input_str[i])
		i += 1
	return sum
	
if __name__ == "__main__":
	res = 0
	input_str = input("Enter string containing numbers : ")
	res = SumOfDigitsFromSting(input_str)
	print res