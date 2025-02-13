# Lyrical Sentiment Analysis and Recommendation 

## Intro
This bot is a personal project being made to take a song and artist to search for,
then analyze those lyrics, as well as get song recommendations from LastFM's API,
to recommend other songs the user may like.

## What it Uses
The program scrapes from [AZ Lyrics](https://www.azlyrics.com/) for song lyrics.
It utilizes a [model](https://huggingface.co/SamLowe/roberta-base-go_emotions) trained by Sam Lowe using 
Google's Go Emotions dataset for advanced sentiment analysis.
Finally, it utilizes LastFM's API to recommend songs similar to the user-provided song

## Coming Up
The initial functionality of the bot is working, however, there is obviously still work to be done for it.
More tests need to be written to ensure total functionality.
I hope to add a user interface eventually, in order to make the bot more user-friendly.
