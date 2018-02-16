"""
WAP to compute value of following expression
expre = a + aa + aaa + aaaa + aaaaa + ......

"""

def ConstructExpression(n, level):
	if level < 1:
		return None
	else:
		expr = 0
		res = 0
		m = 1
		while level:
			res = res + (n * m)
			m = m * 10
			expr = expr + res
			level = level - 1
	return expr
			


if __name__ == "__main__":
	value = input("Enter Number to conpute value : ")
	level = input("Enter expresion level value : ")
	
	result = ConstructExpression(value, level)
	print "Result of Expression : ",result