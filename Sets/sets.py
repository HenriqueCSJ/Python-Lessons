# # farm_animals = {"sheep", "cow", "hen"}

# # print(farm_animals)

# # for animal in farm_animals:
# #     print(animal)

# # print("=" * 40)

# # wild_animals = set(["lion", "tiger", "elephant", "monkery"])

# # print(wild_animals)

# # for animal in wild_animals:
# #     print(animal)

# # farm_animals.add("horse")
# # wild_animals.add("horse")

# # print(wild_animals)
# # print(farm_animals)

# # empty_set = set()
# # range_set = set(range(0, 40, 2))
# # print(range_set)
# # squares = (2, 4, 16, 256)
# # squares_set = set(squares)

# # print(squares_set)

# # even = set(range(0, 40, 2))
# # print(even)
# # print(len(even))

# # squares_tuple = (4, 9, 16, 25)
# # squares = set(squares_tuple)
# # print(squares)
# # print(len(squares))

# # print(even.union(squares))
# # print(len(even.union(squares)))

# # print(even.intersection(squares))
# # print(even & squares)

# # print(sorted(even))

# # print(even.difference(squares))
# # print(even - squares)

# # print("--" * 40)

# # print(sorted(even))
# # print(squares)

# # even.difference_update(squares)
# # print(sorted(even))

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))

# print("Symmetric even minus squares:")
# print(sorted(even.symmetric_difference(squares)))

# squares.discard(4)
# squares.remove(16)

# print(squares)

# try:
#     squares.remove(8)
# except KeyError:
#     print("The number 8 is not in the set.")

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)

# if squares.issubset(even):
#     print("Squares is a subset of even.")

# if even.issuperset(squares):
#     print("Even is a superset of squares.")

# FROZEN SET

even = frozenset(range(0, 100, 2))

print(even)
even.add(3)
