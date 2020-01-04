
"""
Generators: A object which can generate values on the fly.
1. Write a function with yield keyword
2. Generator expression
3. Memory efficient
"""


def simple():
    x  = yield 10
    print(x)
    yield 20

gen = simple()
x = gen.send(None)
print(x)
#print(next(gen))

"""
def gen_values(start, end):
    while start < end:
        step = yield start
        print("herere")
        if step is not None:
            start = start + step
        else:
            start += 1

def initfinite():
    while True:
        yield


gen = gen_values(0, 10)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print("")


gen = gen_values(0, 10)
print(next(gen))
gen.send(None)

print(gen.send(3))
print(next(gen))
#gen.send(3)
#print(next(gen))

for i in initfinite():
    print("going")
"""
