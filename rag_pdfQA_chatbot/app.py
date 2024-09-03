import streamlit as st
from PyPDF2 import PdfReader
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from io import BytesIO

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("himmeow/vi-gemma-2b-RAG")
model = AutoModelForCausalLM.from_pretrained(
    "himmeow/vi-gemma-2b-RAG",
    device_map="auto",
    torch_dtype=torch.bfloat16
)

# Use GPU if available
if torch.cuda.is_available():
    model.to("cuda")

# Streamlit app layout
st.set_page_config(page_title="📄 PDF Query App", page_icon=":book:", layout="wide")
st.title("📄 PDF Query App")
st.sidebar.title("Upload File and Query")

# Sidebar: File Upload
uploaded_file = st.sidebar.file_uploader("Upload your PDF file", type="pdf")

# Sidebar: Query Input
query = st.sidebar.text_input("Enter your query:")

# Sidebar: Submit Button
if st.sidebar.button("Submit"):
    if uploaded_file and query:
        # Read the PDF file
        pdf_text = ""
        with BytesIO(uploaded_file.read()) as file:
            reader = PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                pdf_text += text + "\n"

        # Define the prompt format for the model
        prompt = """
        ### Instruction and Input:
        Based on the following context/document:
        {}
        Please answer the question: {}

        ### Response:
        {}
        """

        # Format the input text
        input_text = prompt.format(pdf_text, query, " ")

        # Encode the input text into input ids
        input_ids = tokenizer(input_text, return_tensors="pt")

        # Use GPU for input ids if available
        if torch.cuda.is_available():
            input_ids = input_ids.to("cuda")

        # Generate text using the model
        outputs = model.generate(
            **input_ids,
            max_new_tokens=500,  # Limit the number of tokens generated
            no_repeat_ngram_size=5,  # Prevent repetition of 5-gram phrases
        )

        # Decode and display the results
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.write(response)
    else:
        st.sidebar.error("Please upload a PDF file and enter a query.")

# Footer with LinkedIn link
st.sidebar.write("---")
st.sidebar.write("Created by: [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)")