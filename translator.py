from deep_translator import GoogleTranslator

def translate_text(text, source_lang='auto', target_lang='en'):
    translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    print("Translated Summary:", translated_text)  # Debugging print statement
    return translated_text
