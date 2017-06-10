from math import sqrt

print("Hello, let's find the solutions for your quadratic equation. Be prepared.")

print("I'll ask for the indexes of your quadratic equation: AX**2 + Bx + C = 0 ")
print("Let's go:")

A = int(input("Enter your A index and press enter: "))
B = int(input("Enter your B index and press enter: "))
C = int(input("Enter your C index and press enter: "))

print(
    "All right, your equation should be something like {0}X**2 {1}X {2} = 0".format(A, B, C))
Delta = B**2 - 4 * (A * C)

print("Your delta is equal to {0}".format(Delta))

if Delta < 0:
    print("Your negative Delta does not have a real solution. Sorry! :-(")
else:
    X1 = (-B + sqrt(Delta)) / (2 * A)
    X2 = (-B - sqrt(Delta)) / (2 * A)
    print(
        "The results for your quadratic equation are: X1 = {0:2.4f} and X2 = {1:2.4f}".format(X1, X2))
