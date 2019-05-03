# age = int(input("How old are you? "))

# if age >= 16 and age <= 65 :
#     print("Have a good day of work")

# if (age >= 16) and (age <= 65) : # parênteses por clareza
#     print("Have a good day of work")

# if age <= 16 <= 65:
#     print("Have a good day of work")

# if 15 < age < 66: # entre esses números
#     print("Have a good day of work")

# if (age < 16) or (age > 65):
#     print("Enjoy your free time!")
# else:
#     print("Have a good day of work!")

# x = input("Please, enter some text: ")

# if x:
#     print("You entered '{0}'".format(x))
# else:
#     print("You did not entered anything.")

# print(not True)
# print(not False)

age = int(input("How old are you? "))

if not(age < 18):  # muda para se a idade é maior ou igual que 18 (pq exclui todas as menores que 18)
    print("You are old enough to vote!")
    print("Put an X to the box.")
else:
    print("Please come back in {0} years".format(18 - age))
