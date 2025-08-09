# Simple Spell Checker (Python)

This is a beginner-friendly Python program that checks the spelling of words in a sentence and suggests corrections.  
It uses the [`pyspellchecker`](https://pypi.org/project/pyspellchecker/) library.

---

## 📌 Features
- Detects misspelled words.
- Suggests and replaces them with the most likely correct spelling.
- Works for simple sentences.
- Easy to understand code for beginners.

---

## 📂 Requirements
Make sure you have Python installed, then install the `pyspellchecker` library:

```bash
pip install pyspellchecker
```
🚀 How to Run

    Save the Python code in a file, for example spell_checker.py.

    Open a terminal in the same directory.

    Run the program:

```bash
python spell_checker.py
```

💻 Example Usage

Enter text to check (or 'q' to quit): Ths is a smple progrm

Correcting "Ths" to "This"
Correcting "smple" to "simple"
Correcting "progrm" to "program"
Original text: Ths is a smple progrm
Corrected text: This is a simple program

📜 How It Works

    The program splits the entered text into words.

    It checks each word against the dictionary in pyspellchecker.

    If a word is misspelled, it replaces it with the most likely correct spelling.

    It displays both the original and corrected text.

🛠 Future Improvements

    Handle punctuation properly.

    Add grammar checking.

    Suggest multiple possible corrections.

📄 License

This project is free to use and modify for learning purposes.

If you want, I can also make a **version with punctuation handling** and update this README so it shows more polished examples. That way it works more like a real spell checker.
