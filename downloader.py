import requests
from bs4 import BeautifulSoup

class Downloader:
    """
        Helper class to download all songs from mp3clan.de
    """
    
    base_url = "http://mp3clan.de/mp3/"

    def create_url(self, song):
        url = self.base_url + "_".join([song.Artist] + song.Name.split(' '))
        return url

    def get_song(self, song):

        url = self.create_url(song)

        r = requests.get(url)

        soup = BeautifulSoup(r.text.encode('utf-8'))

        divs = soup.find_all('div')
        divs = [x for x in divs if x.has_attr('class') and x.has_attr('id')]
        div = [x for x in divs if 'unplaying' in x['class'] and x['id'] == "mp3list"][1]

        
        download = div.div.div.contents[-2]

        print(download.a['href'])

        """Find a way to download the song from the given url"""