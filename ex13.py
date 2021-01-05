# Exercise 13
# Parameters, Unpacking, Variables

from sys import argv

# the value for argv pass from command line when the script called.
# for example: python3 ex13.py value1 value2 value3
script, first, second, third = argv

print("The script is called:",script)
print("My first varaible is:",first)
print("My second varaible is:",second)
print("My third varaible is:",third)
print("This is argv variable value: ",argv)
print("The type of argv is",type(argv))
print("The lenght of argv is",len(argv))
print("Wow! argv is a list.")