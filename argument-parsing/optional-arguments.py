import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "f:m:")

print(opts)
print(args)

for opts, args in opts:
  if opts == "-f":
    filename = args
  elif opts == "-m":
    message = args

with open(filename, "w+") as f:
  f.write(message)

# python optional-arguments.py test.txt Hello\ World

# python optional-arguments.py -f test.txt -m Hello\ World