# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (
    2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

# album, band, release, track1, track2, track3, track4 = imelda
album, band, release, tracks = imelda

print("Album: {0}, Band: {1}, Release Year: {2}".format(album, band, release))

for i in tracks:
    print("\t{}".format(i))

for i in tracks:
    track, title = i
    print("\tTrack number {}, Title: {}".format(track, title))