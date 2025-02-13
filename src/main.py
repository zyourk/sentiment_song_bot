import web_scraper
from web_scraper import LyricNotFound
import sentiment_analyzer
import lastfm

"""
The main script that will run and utilize the other files
for functionality. Currently continually asks user for songs
and outputs their lyrics. This is simply the implementation of the first
step of the process
"""

#While loop to keep it continually running
while(True):
    print("Please enter the artist name")
    artist = input()
    print("Please enter the song name")
    song = input()

    try:
        lyrics = web_scraper.get_lyrics(artist, song)
        print(sentiment_analyzer.analyze(lyrics))
        print(f"For this song, I recommend: \n{lastfm.get_formatted_recs(artist, song)}")
    except LyricNotFound as e:
        print(e.to_string())