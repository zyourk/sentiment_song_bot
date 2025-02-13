import requests
import os
from dotenv import load_dotenv

"""
File that will be responsible for grabbing 
similar songs utilizing LastFM's API.
"""

load_dotenv()

API_KEY = os.getenv("WORKING_KEY")
USER_AGENT = "SentimentBot"

BASE_URL = "https://ws.audioscrobbler.com/2.0/"

#Gets the raw filtered data from the json we get
#from LastFM's getSimilar method
def get_similar_tracks(artist, track):
    headers = {
        "User-Agent": USER_AGENT
    }

    params = {
        "method": "track.getSimilar",
        "api_key": API_KEY,
        "artist": artist,
        "track": track,
        "limit": 5,
        "format": "json"
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if "similartracks" in data and "track" in data["similartracks"]:
            return [
                {
                    "name": t["name"],
                    "artist": t["artist"]["name"],
                    "url": t["url"]
                }
                for t in data["similartracks"]["track"]
            ]
        else:
            return {"error": "No similar tracks found"}
    else:
        return {"error": "Failed to fetch data"}

#Properly formats the raw data in a nice string format
#for the user to read
def get_formatted_recs(artist, track):
    similar_tracks = get_similar_tracks(artist, track)
    formatted_recs = ""
    for track in similar_tracks:
        formatted_recs += f"{track['name']} by {track['artist']}: {track['url']}\n"
    return formatted_recs