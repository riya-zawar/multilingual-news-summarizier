from utils.web_scrapping import get_content_from
from text_preprocessing import preprocess_text
from model import summarize_text

def main(url):
    text = get_content_from(url)
    sentences, words = preprocess_text(text)
    summary = summarize_text(sentences, words)

    return summary

url = "https://en.wikipedia.org/wiki/Natural_language_processing"
summary = main(url)
print(summary)