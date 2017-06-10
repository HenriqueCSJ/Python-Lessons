# for i in range(1, 20):
#     print("i is now {0}".format(i)) # i = index

number = "9.445.342.777.908.999.567"
cleanNumber = ''
for i in range(0, len(number)):  # len = comprimento de uma string
    #    print(number[i])
    if number[i] in "0123456789":
        cleanNumber = cleanNumber + number[i]
newNumber = int(cleanNumber)
print("The number is {0}.".format(newNumber))
