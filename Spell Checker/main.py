from spellchecker import SpellChecker

class SpellCheck:
    def __init__(self):
        # Create a SpellChecker object
        self.spell = SpellChecker()

    def check_spelling(self, text):
        # Split the text into words
        words = text.split()
        corrected_words = []

        # Go through each word in the sentence
        for word in words:
            # Get the most likely correct spelling
            corrected_word = self.spell.correction(word)

            # If the word is misspelled, show the correction
            if corrected_word != word:
                print(f'Correcting "{word}" to "{corrected_word}"')
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)

        # Join the corrected words back into a sentence
        return " ".join(corrected_words)

    def run_spell_check(self):
        print("\n--- Simple Spell Checker ---")
        while True:
            # Ask the user for input
            text = input("Enter text to check (or 'q' to quit): ")

            # Exit if the user types 'q'
            if text.lower() == 'q':
                print("Exiting spell checker...")
                break

            # Check the spelling and print results
            corrected_text = self.check_spelling(text)
            print(f'Original text: {text}')
            print(f'Corrected text: {corrected_text}')


# Start the program
if __name__ == "__main__":
    spell_checker = SpellCheck()
    spell_checker.run_spell_check()
