# Write a small program to ask for a name and age
# When both values have been entered, check if the person
# is the right age to go on a 18-30 holiday (they must be over(
# 18 and under 31).
# If they are, welcome them to the holiday, otherwise, print
# a polite message refusing entry.

name = input("Please, what is your name? ")
age = int(input("Please, enter you age: "))

if (18 <= age < 31):
    print("Hello, {0}, be welcome to the holiday!".format(name))
    print("Enjoy your stay!")
else:
    if (age <= 18):
        print("I'm sorry, {0}, but you have to be between 18 and 30 years to "
              "come. Come back in {1} years".format(name, 18 - age))
    else:
        print("I'm sorry, {0}, but you have to be between 18 and 30 years to "
              "come. You are {1} year(s) late.".format(name, age - 30))
