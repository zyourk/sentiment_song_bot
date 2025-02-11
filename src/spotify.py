import requests
import json
import base64
import os
from dotenv import load_dotenv

"""
Note that this does function correctly due to Spotify deprecating their API.
Unfortunately, Spotify cut the functionality of much of their API, including the recommendations function,
so I can no longer use this for the project. I will leave the residual code here as "proof of concept," 
even though there are no functioning concepts here. Song IDs are successfully grabbed, but that's about
all that was relevant to implement here. I will work out a new way to get recommendations working, but
this will remain in the meantime.
"""

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_str = client_id + ":" + client_secret
    auth_bytes = auth_str.encode("utf-8")
    auth_b64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_b64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    return json_result["access_token"]

token = get_token()

def get_auth_header():
    return {"Authorization": "Bearer " + token}

def get_song_id(song, artist):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header()
    query = f"?q={song}+{artist}&type=track&limit=1"

    query_url = url + query
    result = requests.get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    track_id = json_result[0]["id"]
    return track_id

def get_song_recs(song, artist):
    url = "https://api.spotify.com/v1/recommendations"
    headers = get_auth_header()
    track_id = get_song_id(song, artist)
    query = f"?seed_tracks={track_id}"

    query_url = url + query
    result = requests.get(query_url, headers=headers)
    json_result = json.loads(result.content)
    return json_result