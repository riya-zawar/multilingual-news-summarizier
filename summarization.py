from lsa_summarizer import LsaSummarizer
import nltk

from nltk.corpus import stopwords

def summarize_text(text, summary_length=3, language='english'):
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)

    summarizer = LsaSummarizer()
    stopwords_list = stopwords.words(language)
    summarizer.stop_words = stopwords_list

    summary = summarizer(text, summary_length)

    return summary

source_file = "original_text.txt"
with open(source_file, "r", encoding='utf-8') as file:
    text = file.read()

print(summarize_text(text,language='portuguese'))