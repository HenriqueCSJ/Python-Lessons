# number = "9.445.342.777.908.999.567"
# cleanNumber = ''

# for char in number:
#     if char in "0123456789":
#         cleanNumber = cleanNumber + char

# newNumber = int(cleanNumber)
# print("The number is {0}".format(newNumber))

# for state in ("not pinin", "no more", "a stiff", "bereft of life"):
#     print("This parrot is " + state)

# for i in range(0, 100, 5):
#     print("i is equal to {}".format(i))

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("==================")