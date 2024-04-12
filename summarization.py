from lsa_summarizer import LsaSummarizer
import nltk

from nltk.corpus import stopwords

def summarize_text(text, summary_length=30, language='english'):
    summary=""
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)

    summarizer = LsaSummarizer()
    stopwords_list = stopwords.words(language)
    summarizer.stop_words = stopwords_list

    summary = summarizer(text, summary_length)

    return summary
