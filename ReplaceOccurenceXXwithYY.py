'''
WAP to accept statment from user and replace occurence of "not bad" with "good"
ex - 
	"python is not bad" is replace with "python is good"
'''
def ReplaceWith(stmt):
	i = 0
	if "not bad" in stmt:
		i = stmt.find("not bad",)
		stmt = stmt.replace(stmt[i:],"good")
	return stmt	
		
		
if __name__ == "__main__":
	sentence = input("Enter statment : ")
	replace_sentence = ReplaceWith(sentence)
	print "\"{}\" is replace with \"{}\"".format(sentence,replace_sentence)