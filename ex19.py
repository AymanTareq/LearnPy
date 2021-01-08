# Exercise 19. Functions and Variables
# define a function for practice 
def cheese_and_crakers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crakers(20,30)

print("OR, we can use variable from our scripts:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crakers(amount_of_cheese,amount_of_crackers)

print("WE can even do math inside too:")
cheese_and_crakers(10+20, 5*3)

print("And we can combine the two, variables and math:")
cheese_and_crakers(amount_of_cheese+5,amount_of_crackers-10)
