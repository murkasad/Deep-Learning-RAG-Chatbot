#summarizing the closest 2 chunks extracted from vector store

from transformers import pipeline
from config import SUMMARIZER_MODEL, MIN_SUMMARY_LEN, MAX_SUMMARY_LEN

def load_summarizer():
    return pipeline("summarization", model=SUMMARIZER_MODEL)

def summarize_text(text, summarizer):
    if not text or not text.strip(): #if input text is empty or even if we remove spaces still empty
        raise ValueError("Input text for summarization is empty.")

    output = summarizer(
        text,
        repetition_penalty=5.0,
        length_penalty=0.3,
        min_length=MIN_SUMMARY_LEN,
        max_length=MAX_SUMMARY_LEN
    )

    return output[0]["summary_text"] #pipeline returns alot of type of dictionaries, we only need the short summary from it so we use [0] and "summary_text"
