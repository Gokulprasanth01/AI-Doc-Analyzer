import os
import streamlit as st
from groq import Groq
import pandas as pd
from preprocess import extract_text_from_pdf, preprocess_text
from analyze import analyze_text
from summarization import summarize_text

# Initialize Groq client with the API key
client = Groq(api_key="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")

# Set up file upload
st.title('AI Legal Document Analyzer')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Function to classify document using Groq's llama3-8b-8192 model
def classify_document(summary):
    if not isinstance(summary, str):
        raise ValueError("Input to classify_document must be a string")

    # Use Groq API to classify the document summary
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {"role": "user", "content": f"Summary: {summary}\n\nBased on this summary, can you tell me the type of document?"},
            {"role": "assistant", "content": "Provide a single-word document type."}          
        ],
        temperature=1,
        max_tokens=1024,  
        top_p=1,
        stream=True,  # Enable streaming
        stop=None
    )

    document_type = ""
    
    # Accumulate streamed responses
    for chunk in completion:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content:
            document_type += chunk_content

    return document_type.strip()


# Main logic
if uploaded_file is not None:
    # Save file to a temporary location
    with open(f'./{uploaded_file.name}', 'wb') as f:
        f.write(uploaded_file.read())

    # Extract text from the uploaded PDF
    file_path = f'./{uploaded_file.name}'
    text = extract_text_from_pdf(file_path)

    # Preprocess text
    preprocessed_text = preprocess_text(text)

    # Analyze text
    analysis_results = analyze_text(preprocessed_text)

    # Summarize text
    summary = summarize_text(preprocessed_text)

    st.write(f"Summary: {summary}")

    # Ensure summary is a string
    if not isinstance(summary, str):
        st.error('Summary is not a string')
    else:
        # Classify the document type using Groq API
        try:
            document_type = classify_document(summary)
            st.write(f"Document Type: {document_type}")

            # Store results in DataFrame and display
            results_data = {
                'File Name': [uploaded_file.name],
                'Analysis': [analysis_results],
                'Summary': [summary],
                'Document Type': [document_type]
            }
            results_df = pd.DataFrame(results_data)
            st.dataframe(results_df)

            # Optionally save the results as CSV
            csv_path = f"./results/{uploaded_file.name}_results.csv"
            results_df.to_csv(csv_path, index=False)
            st.success(f'Results saved to {csv_path}')

        except Exception as e:
            st.error(f"Error classifying document: {str(e)}")
