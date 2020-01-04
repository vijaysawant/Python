"""
assert :
1. asserts are used to verify and validate conditions
2. assert raises an AssertionError when condition is evaluated False,
3, asserts are used in unittesting/test automation
4. assets are usefull way to catch early dev bugs (shown in Host example)
"""


# Host example here
class Host:
    def __init__(self, hostname, location='us'):
        pass

def connect(host: Host):
    assert isinstance(host, Host), f"Must be an instance of {Host}"
    ...


connect(host='www.google.com')
