fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making soda",
         "lemmon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit",
         "lime": "a sour, green, citrus fruit"}

print(fruit)
print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print("-" * 40)
print(dict(f_tuple))
