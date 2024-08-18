import pandas as pd
import tempfile
import os
from langchain.vectorstores import FAISS
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import GooglePalm
from langchain.schema import Document
import streamlit as st

# Initialize instructor embeddings using the Hugging Face model
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "faiss_index"

def create_vector_db(file):
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
        temp_file.write(file.read())
        temp_file_path = temp_file.name

    # Try different encodings
    encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            # Load data using pandas with the specified encoding
            df = pd.read_csv(temp_file_path, encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("Failed to decode the CSV file with available encodings.")

    # Check if 'prompt' column exists
    if 'prompt' not in df.columns:
        raise ValueError("CSV must contain a 'prompt' column")

    # Convert DataFrame to list of Document objects
    documents = [Document(page_content=row['prompt']) for _, row in df.iterrows()]

    # Create a FAISS instance for vector database from 'documents'
    vectordb = FAISS.from_documents(documents=documents, embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)

    # Clean up the temporary file
    os.remove(temp_file_path)

def get_qa_chain():
    # Access API key from environment variables or Streamlit secrets
    # api_key = os.getenv("API_KEY")  # or use 
    
    api_key = st.secrets["GOOGLE_API_KEY"] # for Streamlit secrets
    
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from the "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    llm = GooglePalm(google_api_key=api_key, temperature=0.2)

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain
