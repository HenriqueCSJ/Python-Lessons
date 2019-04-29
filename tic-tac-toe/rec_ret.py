# # Demonstration
# """Testing functions"""
# # Receive and return values


# def displaymessage(message):
#     """Receives strings and print it"""
#     print(message)


# def give_me_five():
#     """Returns '5'"""
#     five = 5
#     return five


# def ask_yes_no(question):
#     """Asks a YES or NO question"""
#     response = None
#     while response not in ("y", "n"):
#         response = input(question).lower()
#     return response

# # Main


# displaymessage("Here is a test message")

# number = give_me_five()

# print("Here is what I got from give_me_five: {}".format(number))

# answer = ask_yes_no("\nPlease, enter 'y' or 'n': ")
# print("Thank you for entering {}".format(answer))

# input("\nPress the ENTER key to finish")

# Birthday Wishes
# Demonstrates keyword arguments and default parameter values

# Positional parameters

def birthday1(name, age):
    print("Happy birthday, {}!. I hear that you are {} years old today.\n". format(name, age))


def birthday2(name="Henrique", age=1):
    print("Happy birthday, {}!. I hear that you are {} years old today.\n". format(name, age))


birthday1("Maicon", 23)

birthday2()

birthday2(name="Katherine")
