class Song:
    """ Class to represent a song.
    Atributes: :
        title (str): The title of the Song
        artist (Artist): An artist object representing the song's creator.
        duration (int): The duration of the song in sec. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialize the "title" Atributes
            artist (Artist): At Artist object representing the song's creator
            duration (Oprtional(int)): Initial value for the "duration" atribute.
                Will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration
