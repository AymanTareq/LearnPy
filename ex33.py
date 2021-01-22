# Exercise 33

## study drill

def mk_list_of_numbers(start_num,end_num,step):
    numbers = []

    while start_num < end_num+1:
        print(f"At the top i is {start_num}")
        numbers.append(start_num)

        start_num += step
        print("Numbers now:", numbers)
        print(f"At the bottom i is {start_num}")

    print("The numbers: ")

    for num in numbers:
        print(num)


mk_list_of_numbers(0,100,10)

# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i += 1
#     print("Numbers now:", numbers)
#     print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
#     print(num)