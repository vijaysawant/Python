"""
If we have list [2, 7, 11, 15] and target value is 9, then return indexes whose addition is target value
ex- 0th index value is 2, and 1st index value is 7, whose addition is 9
output should  be 0, 1
"""

input_list = [2, 7, 11, 15, -2]
i = 0
j = 0
target = 9
for no in input_list:
    for j in range(len(input_list)):
        if no + input_list[j] == target:
            print(i, j)
    i = i + 1

"""
Output:
[vijay@localhost Arcserver]$ python return_indext_value.py 
(0, 1)
(1, 0)
(2, 4)
(4, 2)
[vijay@localhost Arcserver]$ 
"""
