import requests
import os

from song import Song
from bs4 import BeautifulSoup

class NostalgiaMachineParser():

    """
        Nostalgia Machine HTML Parser
    """

    NOSTALGIAMACHINE = "http://thenostalgiamachine.com/years/{0}.html"

    def __init__(self):
        pass

    def create_soup(self, year):
        r = requests.get(self.NOSTALGIAMACHINE.format(year))
        soup = BeautifulSoup(r.text.encode('utf-8'))
        return soup

    def get_list_of_songs_from_year(self, year):
        soup = self.create_soup(year)
        divs = soup.find_all('div')

        divs = [x for x in divs if x.has_attr('class')]

        vids = [x for x in divs if 'vid' in x['class']]

        songs = []

        for x in vids:
            values = x.div.h3.contents
            s = Song(values[0], values[1].span.get_text(), x.a['href'])

            songs = songs + [s]
        
        return songs


if __name__ == "__main__":
    main()




