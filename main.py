from NostalgiaMachineParser import NostalgiaMachineParser
from downloader import Downloader

def start():
    year = input("Please give the year you want to download: ")
    parser = NostalgiaMachineParser()

    songs = parser.get_list_of_songs_from_year(year)

    dl = Downloader()
    
    #print(songs[0])
    
    for s in songs: 
        print("Downloading: " + str(s))
        dl.get_song(s)
    
    #dl.get_song(songs[1])

if  __name__ == "__main__":
    start()