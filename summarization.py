from newspaper_extraction import extract_article_text
from lsa_summarizer import LsaSummarizer
import nltk
from nltk.corpus import stopwords
from translator import translate_text 

def summarize_text(text, summary_length=30, language='english'):
    summary = ""
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)

    summarizer = LsaSummarizer()
    stopwords_list = stopwords.words(language)
    summarizer.stop_words = stopwords_list

    summary = summarizer(text, summary_length)

    return summary

def summarize_news_article(url):
    # Extracted text
    article_text = extract_article_text(url)
    
    # Summarizing
    summarized_text = summarize_text(article_text)
    
    # Translating
    translated_summary = translate_summarized_text(summarized_text)
    
    return translated_summary
