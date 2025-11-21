import urllib.parse

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

def get_song_id(song, artist, token=token, limit=10):
    headers = {"Authorization": "Bearer " + token}
    base = "https://api.spotify.com/v1/search"
    q = f'track:"{song}" artist:"{artist}"'
    q_enc = urllib.parse.quote_plus(q)
    url = f"{base}?q={q_enc}&type=track&limit={limit}"

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    items = resp.json().get("tracks", {}).get("items", [])

    if not items:
        raise ValueError(f"No Spotify search results for: {song} - {artist}")

    artist_lower = artist.strip().lower()
    song_lower = song.strip().lower()
    for t in items:
        artist_names = [a["name"].strip().lower() for a in t["artists"]]
        if artist_lower in artist_names:
            if t["name"].strip().lower() == song_lower:
                print(t["id"])
                return t["id"]
            candidate_id = t["id"]
            candidate = t

    for t in items:
        if t["name"].strip().lower() == song_lower:
            print(t["id"])
            return t["id"]

    if 'candidate_id' in locals():
        return candidate_id
    print(items[0]["id"])
    return items[0]["id"]

def get_song_recs(song, artist):
    url = "https://api.spotify.com/v1/recommendations"
    headers = get_auth_header()
    track_id = get_song_id(song, artist)
    query = f"?seed_tracks={track_id}"

    query_url = url + query
    result = requests.get(query_url, headers=headers)
    print(result)
    json_result = json.loads(result.content)
    return json_result

get_song_recs(song="some love", artist="dreamcatcher")