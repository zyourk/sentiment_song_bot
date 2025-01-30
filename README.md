## Lyrical Sentiment Analysis and Recommendation 

# Intro
This bot is a personal project being made to take a song and artist to search for,
then analyze those lyrics, as well as get song metadata from Spotify's API, to 
recommend other songs the user may like.

# What it Uses
The program uses a web scraper that scrapes from [AZ Lyrics](https://www.azlyrics.com/) for song lyrics.
It utilizes a [model](https://huggingface.co/SamLowe/roberta-base-go_emotions) trained by Sam Lowe using 
Google's Go Emotions dataset for advanced sentiment analysis.
Finally, it utilizes Spotify's API to get the song metadata, as well as for the recommendation function.
