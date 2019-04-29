age = 38
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(
    31, "January", "March", "May", "July", "August", "Octuber", "December"))

print("My age is %d" % age)  # Old Python 2 format
print("My age is %d, %s %d %s" %
      (age, "Years", 6, "months"))  # %d = inteiro; %s = string

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %
          (i, i**2, i**3))  # %4d aloca 4 espaços para caber a variável

print("Pi is approximately %12.50f" %
      (22 / 7))  # 50 casas decimais de precisão

# Python 3
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(
        i, i**2, i**3))  # valores alinhados à esquerda

print("Pi is approximately {0:12.50f}".format(
    22 / 7))  # 50 casas decimais de precisão
