import PyPDF2
import pyttsx3

engine = pyttsx3.init()

# Open the PDF file
with open('sample.pdf', 'rb') as pdf_file:  # rb - read binary
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''  # Initialize text as an empty string

    # Read each page in the PDF file
    for page in pdf_reader.pages:  # Loop through pages directly
        text += page.extract_text()

engine.say(text)
engine.runAndWait()
