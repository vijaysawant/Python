dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

g = dict_num.get(1)
print("get(1) : {0}\ntype : {1}".format(g, type(g)))
## get(1) : 10
## type : <class 'int'>

i = dict_num.items()
print("\nItems : {0}\ntype : {1}".format(i,type(i)))
## Items : dict_items([(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)])
## type : <class 'dict_items'>
# for itm in i:
#     print(type(itm))     # class 'tuple'>

k = dict_num.keys()
print("\nKeys : {0}\ntype : {1}".format(k,type(k)))
## Keys : dict_keys([1, 2, 3, 4, 5])
## type : <class 'dict_keys'>

v = dict_num.values()
print("\nValues : {0}\ntype : {1}".format(v,type(v)))
## Values : dict_values([10, 20, 30, 40, 50])
## type : <class 'dict_values'>

"""
Output:
=======
get(1) : 10
type : <class 'int'>

Items : dict_items([(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)])
type : <class 'dict_items'>

Keys : dict_keys([1, 2, 3, 4, 5])
type : <class 'dict_keys'>

Values : dict_values([10, 20, 30, 40, 50])
type : <class 'dict_values'>
"""