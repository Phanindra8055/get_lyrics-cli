import re
import urllib.request
from tkinter import *
from bs4 import BeautifulSoup


def get_lyrics(artist, song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    if artist.startswith("the"):    # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html"

    try:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)

        title = re.search(r'(?<=<h1>)([\w\W]+)(?=<\/h1>)', lyrics).groups()

        title = title[0] + '\n\n'

        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<br>','').replace('<br/>','').replace('</div>','').strip()
        lyrics = lyrics.replace('<i>', '').replace('</i>', '').strip()
        lyrics = title + lyrics

        with open('lyrics.txt', 'w') as f:
            f.write(lyrics)

        return  "Lyrics found"
    except Exception as e:
        return "Lyrics Not Found"

