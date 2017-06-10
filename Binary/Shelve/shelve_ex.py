import shelve

# with shelve.open("ShelveTest") as fruit:
#     fruit["Orange"] = "A sweet citrus orange fruit"
#     fruit["Apple"] = "Steve Jobs likes this one"
#     fruit["Grape"] = "A fruit with a very weird name"
#     fruit["Lemmon"] = "A sour yellow ball"
#     fruit["Lime"] = "Does this thing really exists?"

#     print(fruit["Lemmon"])
#     print(fruit["Grape"])

# print(fruit["Lime"])

fruit = shelve.open("ShelfTest")
# fruit["Orange"] = "A sweet citrus orange fruit"
# fruit["Apple"] = "Steve Jobs likes this one"
# fruit["Grape"] = "A fruit with a very weird name"
# fruit["Lemmon"] = "A sour yellow ball"
# fruit["Lime"] = "Does this thing really exists?"

# print(fruit["Lemmon"])
# print(fruit["Grape"])

# fruit["Lime"] = "Great with tequila"

# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     shelf_key = input("Please, enter a fruit: ")
#     if shelf_key == "quit":
#         break
#     description = fruit.get(shelf_key)
#     print(description)

# while True:
#     dict_key = input("Please, enter a fruit: ")
#     if dict_key == "quit":
#         break

#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())
print("-" * 20)

for f in fruit.items():
    print(f)

print(fruit.items())



fruit.close()
# print(fruit)
