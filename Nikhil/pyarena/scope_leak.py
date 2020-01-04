class MyEx(Exception):
     def __del__(self):
         print("I am getting collected")

"""
try:
     a = 10
     raise MyEx('')
     c = 11
except Exception as e:
     b = 20
     print("leaving scope")
else:
     print("no exception raised")


print(a)
print(b)

"""
"""
#####
for i in range(10):
     pass

print(i)

"""

"""
#####
[x**2 for x in range(10)]
print(x)
"""

"""
with open('D:\\pyarena\\TODO') as f:
      pass

print(f)
"""
