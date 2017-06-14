import shelve

books = shelve.open("/Users/henri/Documents/Python/Binary/Shelve/Challenge/book")

books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_tpast": ["beans", "bread"],
                    "scrambled_eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"])
# print(books["recipes"]["scrambled_eggs"])

# print(books["maintenance"]["loose"])
books.close()