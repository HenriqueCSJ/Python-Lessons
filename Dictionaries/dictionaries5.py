fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making soda",
         "lemmon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit",
         "lime": "a sour, green, citrus fruit"}

# print(fruit)
# print("-" * 40)
veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruit, please?"}

# print(veg)
# print("-" * 40)
# veg.update(fruit)
# print(veg)
# my_list = list(veg)
# my_list.sort()

# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)

print(nice_and_nasty)
print("-" * 40)
print(veg)
print("-" * 40)
print(fruit)
print("-" * 40)



