"""
Given two strings, check whether they are anagram to each other. (implement Counter function)
ex: refresh, fresher
"""
def checkAnagram(str1, str2):
    if len(str1) == len(str2):
        cnt_chars1 = Counter(str1)
        cnt_chars2 = Counter(str2)
        if cnt_chars1 == cnt_chars2:
            return True
    return False

def Counter(input):
    """
    Counter function takes string as input and return dictionary
    containing key as character and value as count of character
    :param input: string
    :return: dictionary
    """
    dict = {}
    for ch in input:
        if ch not in dict:
            dict[ch] = 1
        else:
            dict[ch] += 1
    return dict

if __name__ == "__main__":
    str1, str2 = eval(input("Enter 2 strings: "))
    print("Are strings anagram: ", checkAnagram(str1, str2))
