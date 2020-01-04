"""

1. Lambda function:
     - Lambda is single line function
     - Lambda function an0nymous function
     - On the fly
     - expression only
     - very short
     - used as callbacks
"""

"""
def even_criteria(item):
    print(item)
    return (item % 2 == 0)
"""

e = filter(lambda item: item % 2 == 0, range(20))
even_list = list(e)
print(even_list)

o = filter(lambda item: item % 2 != 0, range(20))
odd_list = list(o)
print(odd_list)

employees = [   {
  "id": 6,
  "name": "xyz"
},

{
    "id": 4,
    "name": "abc"
},

{
    "id": 10,
    "name": "pqr"
}

]

def sort_by_id(item):
    return item["id"]

def sort_by_name(item):
    return item["name"]

print(sorted(employees, key=lambda item: item["id"]))
print(sorted(employees, key=lambda item: item["name"]))
