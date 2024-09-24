# AI Document Analyzer

This project is a web-based application that utilizes NLP (Natural Language Processing) models to analyze legal documents. Users can upload PDF files, which are processed to extract text, classify document types, summarize content, and highlight key clauses and entities. The analysis and classification make use of pre-trained transformer models, with an integration to the Groq API for document type classification.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Future Enhancements](#future-enhancements)

## Features
- **PDF Text Extraction**: Extracts text from uploaded PDF documents.
- **Preprocessing**: Cleans and tokenizes extracted text for further analysis.
- **Text Analysis**: Uses a pre-trained BERT model to identify key clauses and entities within the document.
- **Text Summarization**: Summarizes the document using a BART transformer model.
- **Document Type Classification**: Uses the Groq API to classify the document based on its summarized content.
- **Results Export**: Displays the results in a table format and allows users to download them as CSV files.

## Technologies Used
- **Streamlit**: Web framework for the user interface.
- **Transformers (Hugging Face)**: Pre-trained models for token classification (BERT) and text summarization (BART).
- **Groq API**: For classifying document types using advanced AI models.
- **pdfplumber**: For extracting text from PDF files.
- **Pandas**: For managing and displaying tabular data.

## Installation
### Prerequisites
Ensure you have Python 3.7+ and `pip` installed on your machine.

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/legal-document-analyzer.git
    cd legal-document-analyzer
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Obtain the Groq API key from the Groq platform and replace the placeholder in the `app.py` file:
    ```python
    client = Groq(api_key="your_groq_api_key_here")
    ```

4. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Open the application in a browser, typically at `http://localhost:8501`.
2. Upload a PDF file by clicking on the "Choose a PDF file" button.
3. The app will:
   - Extract text from the PDF.
   - Preprocess the extracted text.
   - Analyze the document, identifying key clauses and entities.
   - Summarize the document.
   - Classify the document type using Groq's model.
4. View the results in the app and optionally download them as a CSV file.

## Future Enhancements
- **Improved Document Classification**: Enhance document classification by training custom models.
- **Multi-Language Support**: Extend functionality to handle documents in multiple languages.
- **User Authentication**: Add user authentication for a more secure document handling experience.

This project provides a streamlined interface for legal document analysis using state-of-the-art NLP techniques and transformer models.
