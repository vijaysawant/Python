'''
Program to demonstrate use of positional and optional argumnets in argparse module

positional argument = there is no '-' or '--' in the prefix
optional argument   = thers is '-' or '--' in the prefix
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-verbosity", help = "increase output verbosity")
parser.add_argument("--ver", help = "showing the version")
parser.add_argument("-opt", help = "this is optional argumnet")
parser.add_argument("pos", help = "this is positional argumnet")

args = parser.parse_args()

###
'''
>python positional_and_optional_arguments.py -h
D:\Python Programs\Command Line>python positional_and_optional_arguments.py --help
usage: positional_and_optional_arguments.py [-h] [-verbosity VERBOSITY]
                                            [--ver VER] [-opt OPT]
                                            pos

positional arguments:
  pos                   this is positional argumnet

optional arguments:
  -h, --help            show this help message and exit
  -verbosity VERBOSITY  increase output verbosity
  --ver VER             showing the version
  -opt OPT              this is optional argumnet
'''
####
	
	