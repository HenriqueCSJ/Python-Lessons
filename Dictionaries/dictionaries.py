fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making soda",
         "lemmon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit",
         "lime": "a sour, green, citrus fruit"}

# ( print(fruit)
# print(fruit["orange"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# # Entradas iguais: a última entrada sobrescreve a primeira
# # del fruit["lemmon"]
# # del fruit
# print(fruit)
# fruit.clear()
# print(fruit)
# print(fruit["tomato"]))

# print(fruit)

# while True:  # while True: executa o loop infinitamente porque esta condição sempre retorna o booleano VERDADE
#     dict_key = input("Please, enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)
# if dict_key in fruit:
#     description = fruit.get(dict_key)
#     print(description)
# else:
#     print("Sorry, we dont have a " + dict_key)

# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " fruit " + fruit[snack])
#     print("-" * 40)

# ordered_key = list(fruit.keys())
# ordered_key.sort()

# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# for keys in fruit.keys():
#     print(keys)

# for val in fruit.values():
#     print(val)

# print("-" * 40)

# for key in fruit:  # Mais eficiente
#     print(fruit[key])

# print(fruit.keys())
# print(fruit.values())

fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "Not nice with ice cream"

print(fruit_keys)


