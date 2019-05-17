class Song:
    """ Class to represent a song.
    Attibutes: :
        title (str): The title of the Song
        artist (Artist): An artist object representing the song's creator.
        duration (int): The duration of the song in sec. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an Album using it's tracklist

    Attibutes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The artist reposnible for the album. If not
        specified, default will be "Various Artists". 
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        addSong: Used to add a new song to the Albun's tracklist.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ Ads a song to the tracklist

        Args:
            song (Song): A song to add.
            position (Optional[int]): If specified, the song will be added to
                that position in the tracklist - inserting in between other
                songs if necessary. Otherwise, the song will be added to the
                end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:
    """ basic class to store Artist details
    
    Attributes:
        name (str): The name of the aritst.
        albuns (List[Album]): A list of the albuns by this artist.
            The list include only those albuns in this collection.

    Methods:
        add_album: Use to add a new album to the atist's list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list.

        Args:
            album (Album): Album object to the list.
                If album is already present, it will not be added again.
                (yet to implement)
        """
        self.albums.append(album)

# help(Song.__init__)
help(Album)
