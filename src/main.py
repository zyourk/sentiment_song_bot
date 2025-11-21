import lyrics_genius
import sentiment_analyzer
import lastfm

"""
The main script that will run and utilize the other files
for functionality. 
"""
print("Welcome to version 1 of sentiment analysis and song recommendation.")
print("Please enter the artist name")
artist = input()
print("Please enter the song name")
song = input()

lyrics = lyrics_genius.get_lyrics(artist, song)
if lyrics:
    print(sentiment_analyzer.analyze(lyrics))
    same_artist, different_artist = lastfm.get_formatted_recs(artist, song)
    if not same_artist or not different_artist:
        print("Sorry, it looks like I had issues finding recommendations for your track. Please try again.")
    else:
        print(f"For the same artist, I recommend {same_artist["name"]} by {same_artist['artist']}.")
        print(f"For a different artist, I recommend {different_artist['name']} by {different_artist['artist']}.")
else:
    print("Sorry, I couldn't find lyrics for that song")
    print("""
    This version of the project is only capable of analyzing songs in English.
    If you mistyped your song, please try again.
    If you inputted a foreign song, please try again with an English song.""")