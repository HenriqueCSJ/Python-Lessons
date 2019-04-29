# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

my_text = input("Please, write some text here: ")
vowels = set(("a", "e", "i", "o", "u"))  # Poderia ser frozenset
my_set = set(my_text)
# my_set.difference_update(vowels)
new_set = my_set.difference(vowels)
print(list(new_set))
