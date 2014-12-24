import requests
import webbrowser
from bs4 import BeautifulSoup

class Downloader:
    """
        Helper class to download all songs from mp3clan.de
    """
    
    mp3clan_url = "http://mp3clan.de/mp3/"
    mp3forme_url = "http://mp3for.me/mp3songs/"

    def create_url(self, base_url, song):

        if base_url == self.mp3clan_url:
            url = base_url + "_".join(song.Artist.split(' ') + song.Name.split(' ')) + ".html"
        
        elif base_url == self.mp3forme_url:
            url = base_url + " ".join(song.Artist.split(' ') + song.Name.split(' '))
        
        return url

    def get_page(self, url, song):

        dl_url = self.create_url(url, song)
            
        r = requests.get(dl_url)
            
        soup = BeautifulSoup(r.text.encode('utf-8'))

        return soup


    def get_download_page(self, song):
        soup = self.get_page(self.mp3clan_url, song)    

        divs = soup.find_all('div', {"class": "mp3list-download", "title": "Download"})
        
        if len(divs) > 0:
            return self.create_url(self.mp3clan_url, song)
            #return divs[0].a['href']
        
        soup = self.get_page(self.mp3forme_url, song)

        divs = soup.find_all('div', {"class": "track-title"})
        
        if len(divs) > 0:
            return self.mp3forme_url[:-10] + divs[0].a['href']


    def get_song(self, song):

        download_link = self.get_download_page(song)

        if download_link:
            print(download_link)
            webbrowser.get('firefox').open_new_tab(download_link)

        #divs = [x for x in divs if x.has_attr('class') and x.has_attr('id')]
        #div = [x for x in divs if 'unplaying' in x['class'] and x['id'] == "mp3list"][1]

        
        #download_link = div.div.div.contents[-2].a['href']
        
        #print(download_link)

        """Found! - Find a way to download the song from the given url"""

        