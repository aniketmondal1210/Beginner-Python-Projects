from googletrans import Translator

# Initialize the translator
translator = Translator()

# Get user input
text = input("Enter the sentence/word which is to be translated: ")
source_lang = input("Enter the source language code: ")
target_lang = input("Enter the target language code: ")

# Translate the text
translated = translator.translate(text, src=source_lang, dest=target_lang)

# Display the translated text
print(f"Translated Text: {translated.text}")


"""English: en
Bengali: bn
Hindi: hi
French: fr
Spanish: es"""
