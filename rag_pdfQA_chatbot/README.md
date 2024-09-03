---
title: Rag PdfQA Chatbot
emoji: 👁
colorFrom: purple
colorTo: gray
sdk: streamlit
sdk_version: 1.38.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
# PDF Query Chatbot

![PDF Query Chatbot](https://huggingface.co/datasets/datascientist22/pdf-query-chatbot/preview)

## Overview

The **PDF Query Chatbot** is a Streamlit-based application hosted on Hugging Face Spaces. It allows users to upload a PDF document and ask questions about its content. The chatbot utilizes a transformer model to generate responses based on the text extracted from the PDF.

## Live Demo

You can try the PDF Query Chatbot live here: [PDF Query Chatbot on Hugging Face Spaces](https://huggingface.co/spaces/datascientist22/rag-pdfQA-chatbot)

## Features

- **Upload PDF Files**: Upload PDF files directly from your local machine.
- **Query Input**: Enter questions related to the uploaded PDF content.
- **Text Extraction**: Extracts text from the PDF for querying.
- **Response Generation**: Uses a transformer model to generate answers based on your query and the PDF content.

## How to Use

1. **Upload PDF File**: Use the sidebar to upload a PDF file.
2. **Enter Query**: Type your question related to the PDF content in the query input field.
3. **Submit**: Click the "Submit" button to process the file and get a response.
4. **View Response**: The generated response will be displayed below the input fields.

## Requirements

To run this app locally, ensure you have the following Python packages installed:

- `transformers`: For using pre-trained transformer models.
- `PyPDF2`: For extracting text from PDF files.
- `torch`: PyTorch library for running the model.
- `streamlit`: For the web app interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mldatascientist23/Generative_AI_Projects.git
    cd your-repository
    ```

2. Install the required packages:
    ```bash
    pip install transformers PyPDF2 torch streamlit
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ``