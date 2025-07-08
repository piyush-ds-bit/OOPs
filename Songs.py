class Song:
    """A class to represent a Song.

    Attributes:
        title (str): Name of the song.
        artist (Artist): Name of the artist who has sung the song.
        duration (int): The duration of the songs in seconds. Maybe zero.
    """
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent an album, using it's track list.

    Attributes:
        name (str): name of the artist.
        year (int): year of publishing the song.
        artist (Artist): Artist of the album. If there is no artist,
            the default value to be displayed as "Various Artist"
        tracks (List[Song]): the list of songs on the album.

    Methods:
        addSong: use to add new song to the artist's track list.
        """
    def __init__(self, name , year, artist=None):
        self.name = name
        self .year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Add song to the track list
        Args:
            song (Song):
            position (Optional[int]): if specified, the song will be positioned at a definite position
                in the track list - if necessary.
                Otherwise, the song will be added at the end of the list.
            """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store Artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): The list of albums released by the artist.

    Methods:
        add_album: Use to add new album in a list.
    """
    def __init__(self, name):
        self.name = name
        self.albums = []


    def add_album(self, album):
        """Add a new album to the list.
        Args:
            album (Album): An album object to be added to the list.
                If the album is already present, then it will not be added again (Although it is yet to be implemented).

        """
        self.albums.append(album)


def load_data():
     new_artist = None
     new_album = None
     album_list = []
     with open("albums.txt", "r") as albums:
         for line in albums:
             artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
             year_filed = int(year_field)
             print(artist_field, album_field, year_field, song_field)

if __name__ == "__main__":
    load_data()
