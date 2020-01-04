import numpy as np
from timeit import Timer

size_of_vec = 1000
X_list = range(size_of_vec)
Y_list = range(size_of_vec)
X = np.arange(size_of_vec)
Y = np.arange(size_of_vec)

def pure_python_version():
    Z = [X_list[i] + Y_list[i] for i in range(len(X_list)) ]

def numpy_version():
    Z = X + Y

timer_obj1 = Timer("pure_python_version()", 
                   "from __main__ import pure_python_version")
timer_obj2 = Timer("numpy_version()", 
                   "from __main__ import numpy_version")

print(timer_obj1.timeit(10))
print(timer_obj2.timeit(10))  # Runs Faster!

print(timer_obj1.repeat(repeat=3, number=10))
print(timer_obj2.repeat(repeat=3, number=10)) # repeat to prove it!

'''
D:\Python Programs\NumPy Array in python>python Numpy_demo.py
0.004570834000000024
5.366100000003815e-05
[0.004105948999999998, 0.0033400430000000148, 0.0030403290000000083]
[3.2719999999986094e-05, 1.54440000000311e-05, 1.5704999999976987e-05]

'''