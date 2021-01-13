## Exercise 21. Functions Can Return Something

def add(a,b):
    print("Adding {} + {}".format(a,b))
    return a + b

def subtract(a,b):
    print("Subtracting {} - {}".format(a,b))
    return a - b

def multiply(a,b):
    print("Multipling {} * {}".format(a,b))
    return a * b

def divide(a,b):
    print("Dividing {} / {}".format(a,b))
    return a / b

print("Let's do some math with just functions!!")

age = add(14,2)
height = subtract(36,9)
weight = multiply(25,2)
iq = divide(45,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit , answer it
print("Here is a puzzle.")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("That becomes:",what,"Can you do it by hand?")

# Make a formula to find 'what' value by hand.

reault = age+height-weight*iq/2

print("Result = what:",reault==what)

# Try to make another formula and do it calling fucntion

result2 = height/iq*age+weight*iq-20

what2 = subtract(add(multiply(divide(height,iq),age),multiply(weight,iq)),20)

print(f"Result2: {result2}, What2: {what2}")
print("Do you correctly find what2 value using function: ",result2==what2)