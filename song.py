class Song(object):
    
    def __init__(self, name, artist, link):
        self.Name = name
        self.Artist = artist
        self.Link = link

    def __str__(self):
        return "{0} by {1}".format(self.Name, self.Artist, self.Link)



