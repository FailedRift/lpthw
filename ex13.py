from sys import argv
# Read the WYSS section for how to run this
script = argv[0]
first = argv[1]
second = argv[2]
third = int(argv[3])

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third  modified variable is:", third*third)