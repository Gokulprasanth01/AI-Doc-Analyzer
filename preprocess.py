import pdfplumber

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def preprocess_text(text):
    # Add any necessary preprocessing steps here (e.g., cleaning, tokenizing)
    return text
