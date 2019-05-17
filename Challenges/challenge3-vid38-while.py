import random

highest = 10
answer = random.randint(1, highest)
print(answer)

print("Please, guess a number between 1 and {}".format(highest))
guess = int(input())

if guess == 0:
    print("Good bye")
else:
    if guess == answer:
        print("Well done, you guessed it first time!")
    else:
        while guess != answer:
            if guess < answer:
                print("Please, guess higher!")
            else:
                print("Please, guess lower!")
            guess = int(input())
            if guess == answer:
                print("Well done! You guessed it!")
