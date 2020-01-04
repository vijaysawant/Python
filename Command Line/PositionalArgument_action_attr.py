"""
Program to demonstrate concept of positional argumnet - action attribute
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help = "increase output verbosity", action="store_true")

args = parser.parse_args()

if args.verbosity:
	print("Verbosity turned on")
else:
	print("Verbosity turned off")
	
	
	
###
"""

>python PositionalArgument_action_attr.py --verbosity
Verbosity turned on

>python PositionalArgument_action_attr.py
Verbosity turned off

>python PositionalArgument_action_attr.py -v
Verbosity turned on

"""
###