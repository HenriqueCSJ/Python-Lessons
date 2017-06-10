import shelve

with shelve.open("/Users/henri/Documents/Python/Binary/Shelve/bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 Dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    del bike["Colour"]

    for key in bike:
        print(key)
    print("=" * 40)
    print(bike["engine_size"])
    print(bike["colour"])
