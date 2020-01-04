import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Name", help="enter name of user", type = str)
parser.add_argument("Num", help="enter number of user", type = int)

arguments = parser.parse_args()

print arguments.Name
print arguments.Num

