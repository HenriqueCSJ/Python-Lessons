locations = {0: "You're sitting in front of the computer learning Python.",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside of a building, a well house for a small stream.",
             4: "You are in a valley beside a stream.",
             5: "You are in the forest."}

exits = [{"Q", 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = exits[1]["E"]

print(loc)
