"""
PEP8
Simple rule -
Function
  - syntax, args, kwargs, return types, return multiple values

1. Functions are first class objects
  - Can be passed as an argument to another Function
  - Can be returned from a Function
  - can be assigned to a variable
  - function can be nested
2. Decorator

Given any string add header tag <h1> </h1>
   input : Welcome
   output : <h1> Welcome </h1>
 """

from functools import wraps

def italic(original_func):
    @wraps(original_func) # Recommended if something depends on original function attributes, metadata
    def wrapped(employee_name):
        res = original_func(employee_name)
        return "<i>" + res + "</i>"
    return wrapped

import time

def timeit(original_func):
    @wraps(original_func) # Recommended if something depends on original function attributes, metadata
    def wrapped(employee_name):
        start = time.time()
        res = original_func(employee_name)
        end = time.time() - start
        print(f"finished in {end}")
        return res
    return wrapped

def headify(original_func):
    @wraps(original_func)
    def wrapped(employee_name):
        res = original_func(employee_name)
        return "<h1>" + res + "</h1>"
    return wrapped

@timeit
@italic
@headify # This is equivalen to : google_welcome = headify(google_welcome)
def google_welcome(employee_name):
    time.sleep(2)
    return "Welcome " +  employee_name + " to Google"

@italic
@headify # # This is equivalen to : amazon_welcome = headify(amazon_welcome)
def amazon_welcome(employee_name):
    return "Welcome " +  employee_name + " to Amazon"

"""
google_welcome = headify(google_welcome)
google_welcome = italic(google_welcome)

amazon_welcome = headify(amazon_welcome)
amazon_welcome = italic(amazon_welcome)
"""
print(google_welcome.__name__)

print(google_welcome("Vijay Sawant"))
print(amazon_welcome("Sir Vijay Sawant"))



# snap
