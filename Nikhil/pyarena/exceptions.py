"""
Exception:
1. Error condition
2. SytaxError - which is static time
2. Every exception is runtime exception

Exception handling:
1. Catching an exception and perform some action
2. Exception propogation
   - If these is an unhadled exception propogate to top level function.
   - Cause program to break and exit
3. Traceback - any exception is thrown it associates a Traceback with it,
    - Tell the information about exception, function stack, line number, Exception messages, Types

4. Older python 2.7 - Traceback that was only of last exceptions. But in python 3 your will see all exception chained.

5. Exception are objects and they are types
  - Top most exception class/type is "Exception"
  - Every exception can be handled by Exception
  - Exceptions object can treated as any other object (first class objects)
    However, they can be used "raise" keyword.
"""

"""
1. SyntaxError, IndentationError
2. IndexError, ValueError, AssertionError, NameError, TypeError, IndentationError, KeyError,
"""

d = {}
l = []

class BadProgramming(Exception):
    pass

import sys
import traceback

d = {4: 0}

def test():
    try:
        d[4]
    except IndexError as e:
        print(e)
        traceback_string = traceback.format_exc()
    else:
        print("in else block")
    finally:
        print("in finally")

    # cleanup activitvities

def test2():
    test()

def main():
    test2()


main()
