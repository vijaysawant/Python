def RunningLengthEncoding(input_string):
	i = 0
	cnt = 1
	string = ""
	while i < len(input_string):
		
		if i < len(input_string) and input_string[i] == input_string[i+1]:
			cnt += 1
		else:
			if cnt > 1:
				string = string+input_string[i]+str(cnt)
			cnt = 1
		i+=1
	print string
	
RunningLengthEncoding("aaabbbabc")