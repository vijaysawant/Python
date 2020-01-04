

"""
input : any string
output:
  <span> <i><b>hello</b></i> </span> <

"""
from functools import wraps

def tagify(*args):
    print(args)
    def wrapper(original_func):
        @wraps(original_func) # Recommended if something depends on original function attributes, metadata
        def wrapped(string):
            print(string)
            res = original_func(string)
            for tag in args:
                print(tag)
                start_tag = f'<{tag}>'
                end_tag = f'</{tag}>'
                res = start_tag + res + end_tag
            print("ending call wrapped")
            return res
        print("ending call wrapper")
        return wrapped
    print("ending tagify call")
    return wrapper


@tagify("b", "i", "span", "div")
def text(string):
    return string


#print(tagify("b", "i","span", "div")(text)("hello"))
