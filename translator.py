from deep_translator import GoogleTranslator

def translate_text(text: str, target_lang: str = 'en') -> str:
    """
    Translates text to the target language using Google Translate.

    Args:
        text (str): The text to translate.
        target_lang (str, optional): The target language. Defaults to 'en'.

    Returns:
        str: The translated text.
    """
    # Split the text into chunks of 5000 characters
    chunk_size = 5000
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    translated_chunks = []
    for chunk in chunks:
        # Allow Google Translator to auto-detect source language
        translated_chunk = GoogleTranslator(source='auto', target=target_lang).translate(chunk)
        translated_chunks.append(translated_chunk)

    translated_text = ''.join(translated_chunks)
    return translated_text