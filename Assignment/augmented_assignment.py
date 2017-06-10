number = "9.223.372.036.854.775.807"
cleanNumber = ''

# for i in range(0, len(number)):
#     if number[i] in "0123456789":
#         cleanNumber = cleanNumber + number[i]

for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanNumber += number[i]

newNumber = int(cleanNumber)
print("The number is {}.".format(newNumber))

x = 23
x += 1
print(x)

x -= 20
print(x)