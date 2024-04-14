from deep_translator import GoogleTranslator
import nltk
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')

def detect_language(text):
    words = wordpunct_tokenize(text.lower())
    # Filter out stopwords
    stop_words = set(stopwords.words('english'))  # Assuming English stopwords
    filtered_words = [word for word in words if word.lower() not in stop_words]
    # Calculate frequency distribution of words
    language_guess = nltk.FreqDist(filtered_words).max()
    return language_guess

def translate_text(text, target_lang='en'):
    source_lang = detect_language(text)
    translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    return translated_text
