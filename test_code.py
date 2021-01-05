


# # This script demonstrate the `flush` argument of print() function.
# #!/usr/bin/env python
# #-*- coding: utf-8 -*-

# from __future__ import print_function
# from time import sleep

# string = "The words in this sentence should appear letter by letter."

# print("Please wait if you don't see another sentence appearing below.", end="\n\n")

# for characters in string:
#     # If flush disabled the another line will appear at once and not char by char.
#     print(characters, end="", flush=True)
#     sleep(.1)
# print()
# for i in "Ayman Tareq":
#     print(i,end='',flush=True)
#     sleep(.1)