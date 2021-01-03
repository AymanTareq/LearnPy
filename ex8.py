# exercise 8

formatter = "{} {} {} {}."

print(formatter.format(1, 2, 3, 4))
print(formatter.format("One","two","three","four"))
print(formatter.format("True",True,False,False))
print(formatter.format(formatter,formatter,formatter,formatter))

print(formatter.format(
    "Hey,",
    "this is",
    "Ayman",
    "Tareq"
))