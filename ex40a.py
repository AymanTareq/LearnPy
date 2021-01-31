### Modules, Classes, and Objects
# Exercise 40a

mystuff = {'apple':"I AM APPLES!"}
print(mystuff['apple'])


# dict style
mystuff['apple']        # get apple from dict

import mystuff
## module style
mystuff.apple()         # get apple from the module
print(mystuff.tangerine)       # same thing, it's just a variable

### Class style
thing = mystuff.MyStuff()
thing.apple()
print(thing.tangerine)


