# # print(range(100))

# # my_list = list(range(100))
# # print(my_list)

# # even = list(range(0, 10000, 2))
# # odd = list(range(1, 10000, 2))

# # print(even)
# # print(odd)

# # my_string = "abcdefghijklmnopqrstuvwxyz"
# # print(my_string.index("e"))
# # print(my_string[4])

# # small_decimals = range(0, 10)
# # print(small_decimals)
# # print(small_decimals.index(3))

# # odd = range(1, 10000, 2)
# # print(odd)

# # print(odd[985])

# # sevens = range(7, 1000000, 7)
# # x = int(input("Please, enter a positive number less than one million: "))

# # if x in sevens:
# #     print("{} is divisible by 7!".format(x))

# # my_range = small_decimals[::3]
# # print(my_range)

# decimals = range(0, 100)
# print(decimals)

# my_range = decimals[3:40:3]
# print(my_range)

# for i in my_range:
#     print(i)

# print("=" * 40)

# for i in range(3, 40, 3):
#     print(i)

# print(my_range == range(3, 40, 3))

# print(range(0, 5, 2) == range(0, 6, 2))
# list1 = list(range(0, 5, 2))
# list2 = list(range(0, 6, 2))
# print(list1)
# print(list2)

# r = range(0, 100)
# print(r)

# # for i in r[::-2]:
# #     print(i)

# for i in range(99, 0, -2):
#     print(i)

# print(range(0, 100)[::-2] == range(99, 0, -2))  # true

backstring = "egaugnal lufrewop yrev a si nohtyP"
print(backstring[::-1])

r = range(1, 11)

for i in r[::-1]:
    print(i)

o = range(0, 100, 4)
list_o = list(o)
print(o)
print(list_o)

p = o[::5]
list_p = list(p)
print(p)
print(list_p)

my_string = "This is just a test to see how lists work"

for texts in my_string[::-1]:
    print(texts)


