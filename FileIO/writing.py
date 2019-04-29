# cities = ["Rio de Janeiro", "Pernambuco", "Porto Alegre", "Paris", "London", "Ottawa"]

# with open("/Users/henri/Documents/Python/FileIO/cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities = []
# with open("/Users/henri/Documents/Python/FileIO/cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip("\n"))  # Remove caracteres do começo ou do final
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the plug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

# with open("/Users/henri/Documents/Python/FileIO/imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("/Users/henri/Documents/Python/FileIO/imelda3.txt", "r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda

print(title)
print(artist)
print(year)
print(tracks)
