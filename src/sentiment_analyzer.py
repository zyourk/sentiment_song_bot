from transformers import pipeline, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "SamLowe/roberta-base-go_emotions",
    model_max_length=512,
    truncation=True
)

pipe = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    tokenizer=tokenizer,
    truncation=True,
    max_length=512
)

def analyze(lyrics):
    try:
        lyrics = format_lyrics(lyrics)
        sentiment = pipe(lyrics)[0]
        label = sentiment["label"]
        score = sentiment["score"]
        return f"The primary emotion detected was {label} with a score of {score * 100:.2f}%"
    except Exception as e:
        return f"We were unable to analyze the lyrics for this song. Please try another song. Error: {e}"

def format_lyrics(lyrics):
    lyrics = lyrics.replace("\n", " ")
    return "".join(c for c in lyrics if c.isalnum() or c == ' ')

"""
Note for the final except block: This exception is very vague, however
    1. The stack trace reports an InvalidArgumentError and an IndexError, but neither were successfully caught
    2. I am still in the process of debugging this error. The model seems to add a lot of padding to the lyrics, for example
        turning Happy by Pharrell Williams (which should only have 473 tokens) into 690 tokens. Until I can 
        successfully debug this, there is a placeholder generic Exception and a sad "Try again!" message
"""