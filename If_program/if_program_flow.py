# name = input("Enter your name: ")
# age = int(input("How old are you, {0}? : ".format(name)))
# print(age)

# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please, came back in {0} years".format(18 - age))

print("PLease, guess a number between 1 and 10: ")
guess = int(input())  # Lê um número

if guess != 5:  # Primeiro teste, se o número for diferente de 5...
    if guess < 5:  # Se o número diferente de 5 for menor que 5...
        print("Please, guess higher!")  # imprima essa mensagem
    # Então, se o número é diferente de 5, mas não é menor que 5, ele é maior
    # (>) que 5
    else:
        print("Please, guess lower!")  # Por isso, tente chutar um número menor
    guess = int(input())  # Segunda chance de tentar
    if guess == 5:  # Se a pessoa acertar que o número é 5...
        print("Well done! You guessed it!")  # Então imprima isso
    else:  # Caso contrário...
        print("Sorry, you have not guessed correctly.")  # Imprima isso
else:  # Mas se a pessoa acertar de primaira
    print("Well done! You guessed it first time!")  # imprima isso
