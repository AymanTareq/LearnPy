# exercise 12

age = input("\tHow old are you? ")
height = input("\tHow tall are you? ")
weight = input("\tHow much do you weigh (kg)? ")

print("\tSo, you're {} years old, {} tall and {} kg heavy.".format(age,height,weight),flush=False)

# Python short documentation in command line.
# command: python3 -m pydoc 'keyword/function_name'
# for example:
#   to know about print function: python3 -m pydoc print
#   to know about input function: python3 -m pydoc input

print('hey, you are',input("Name:?"))       # cool syntax!