# list_1 = []
# list_2 = list()

# print("List 1 is {}".format(list_1))
# print("List 2 is {}".format(list_2))

# if list_1 == list_2:
#     print("The lists are equal!")

# print(list("The lists are equal!"))

# even = [2, 4, 6, 8]
# another_even = list(even)
# #another_even.sort(reverse=True)
# another_even = sorted(even, reverse=True)

# print(even)
# print(another_even is even) # IS é um teste de memória, == é um teste de
# conteúdo

# #as variáveis são objetos, então, modificando uma, a outra também se modifica

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

print(numbers)

for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value)
