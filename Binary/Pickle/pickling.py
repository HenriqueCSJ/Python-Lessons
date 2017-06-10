import pickle

# imelda = ("More Mayhem",
#           "Imelda May",
#           "2011",
#           ((1, "Pulling the rug"),
#            (2, "Psycho"),
#            (3, "Mayhem"),
#            (4, "Kentysh Town Valtz")))

# with open("/Users/henri/Documents/Python/Binary/Pickle/imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open("/Users/henri/Documents/Python/Binary/Pickle/imelda.pickle", "rb") as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)

# print(imelda2)

# album, artist, year, tracks = imelda2

# print(album)
# print(artist)
# print(year)
# print(tracks)

# for track in tracks:
#     track_number, track_title = track
#     print(track_number, track_title)

imelda = ("More Mayhem",
          "Imelda May",
          "2011",
          ((1, "Pulling the rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentysh Town Valtz")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("/Users/henri/Documents/Python/Binary/Pickle/imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(odd, pickle_file, protocol=0)
    pickle.dump(2998303, pickle_file, protocol=0)

with open("/Users/henri/Documents/Python/Binary/Pickle/imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, tracks = imelda2

print(album)
print(artist)
print(year)
print(tracks)

for track in tracks:
    track_number, track_title = track
    print(track_number, track_title)

print("=" * 40)

for i in even_list:
    print(i)

print("-" * 40)

for j in odd_list:
    print(j)

print("+" * 40)

print(x)



