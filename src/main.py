from web_scraper import LyricScraper
from web_scraper import LyricNotFound

"""
The main script that will run and utilize the other files
for functionality. Currently continually asks user for songs
and outputs their lyrics. This is simply the implementation of the first
step of the process
"""

#Define our scraper
scraper = LyricScraper()

#While loop to keep it continually running
while(True):
    print("Please enter the artist name")
    artist = input()
    print("Please enter the song name")
    song = input()

    try:
        lyrics = scraper.get_lyrics(artist, song)
        print(lyrics)
    except LyricNotFound as e:
        print(e.to_string())