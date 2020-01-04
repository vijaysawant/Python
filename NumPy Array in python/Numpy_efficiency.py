
###
#
#	Python Lists vs. Numpy Arrays - What is the difference?
#
##

import time
import numpy as np

size_of_vec = 1000

def pure_python_version():
    t1 = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = [X[i] + Y[i] for i in range(len(X)) ]
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    return time.time() - t1


t1 = pure_python_version()
t2 = numpy_version()
print(f"{time_1} seconds and {time_2} seconds")
#print("Numpy is in this example " + str(t1/t2) + " faster!")

'''
0.0002446174621582031 0.00020933151245117188
Numpy is in this example 1.1685649202733486 faster!
'''
