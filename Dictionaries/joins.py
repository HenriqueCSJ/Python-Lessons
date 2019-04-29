myList = ["a", "b", "c", "d"]
newString = ""

# for c in myList:
#     newString += c + ", "
newString = ", ".join(myList)
print(newString)

letters = "abcdefghijklmnopqrstuvwxyz"
newString = ", ".join(letters)
print(newString)

numbers = "1234567890"
newString2 = " Mississippi, ".join(numbers)
print(newString2)