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


OR


import pyttsx3           # For text-to-speech
import PyPDF2            # For reading PDF files

# Open the PDF file
book = open("sample.pdf", "rb")
# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(book)
# Count the total number of pages
pages = len(pdf_reader.pages)
print("Total pages:", pages)
# Create a text-to-speech engine
speaker = pyttsx3.init()
# Read each page one by one
for num in range(pages):
    page = pdf_reader.pages[num]        # Get the page
    text = page.extract_text()          # Extract text from the page

    if text:                            # Check if there's any text
        speaker.say(text)              # Speak the text
# Speak all the text
speaker.runAndWait()
# Close the PDF file
book.close()
