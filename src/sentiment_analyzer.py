from transformers import pipeline
pipe = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")


#Simply uses the trained model to analyze lyrics
def analyze(lyrics):
    try:
        lyrics = format_lyrics(lyrics)
        sentiment = pipe(lyrics)[0]
        label = sentiment["label"]
        score = sentiment["score"]
        return f"The primary emotion detected was {label} with a score of {score:.3f}"
    except Exception:
        return "We were unable to analyze the lyrics for this song. Please try another song."

#Helpful for reducing the length of the tokenized sequence, so longer songs can be analyzed
def format_lyrics(lyrics):
    lyrics = lyrics.replace("\n", " ")
    return "".join(c for c in lyrics if c.isalnum or c == ' ')
"""
Note for the final except block: This exception is very vague, however
    1. The stack trace reports an InvalidArgumentError and an IndexError, but neither were successfully caught
    2. I am still in the process of debugging this error. The model seems to add a lot of padding to the lyrics, for example
        turning Happy by Pharrell Williams (which should only have 473 tokens) into 690 tokens. Until I can 
        successfully debug this, there is a placeholder generic Exception and a sad "Try again!" message
"""