class Song(object):
    
    def __init__(self, name, artist):
        self.Name = name
        self.Artist = artist

    def __str__(self):
        return "{0} by {1}".format(self.Name, self.Artist)



