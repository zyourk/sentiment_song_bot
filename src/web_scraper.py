import requests
from bs4 import BeautifulSoup

#Method that retrieves the lyrics by standardizing the URL parameters,
#ensuring the response is successful, then parsing the html for lyrics
def get_lyrics(artist, song):
    #AZLyrics does not include "the" if it is the first word in an artist's name
    artist_words = artist.split()
    if artist_words[0].lower() == "the":
        artist = "".join(artist_words[1:])

    artist = "".join(filter(str.isalnum, artist))
    song = "".join(filter(str.isalnum, song))
    url = f"https://www.azlyrics.com/lyrics/{artist}/{song}.html"

    response = requests.get(url)
    if(response.status_code != 200):
        raise LyricNotFound(f"Could not find lyrics for {artist} - {song}. Please ensure it was typed correctly, or try another song.")

    soup = BeautifulSoup(response.text, "html.parser")
    sections = soup.find_all("div", class_ = None)      #In AZLyrics, the lyrics are in an unclassified divider class

    lyrics = "\n".join([divs.text for divs in sections])

    return lyrics.strip()

"""
Exception class to be raised when lyrics are unable
to be found, whether it be by user error or because
AZLyrics does not have those lyrics.
"""
class LyricNotFound(Exception):
    def __init__(self, message):
        self.message = message

    def to_string(self):
        return self.message