import nltk
nltk.download('punkt')
nltk.download('wordnet')

import streamlit as st
from pathlib import Path
from streamlit_chat import message
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
import pandas as pd
import tempfile
import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import GooglePalm
from langchain.schema import Document

# Initialize instructor embeddings using the Hugging Face model
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "faiss_index"

def create_vector_db(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
        temp_file.write(file.read())
        temp_file_path = temp_file.name

    encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            df = pd.read_csv(temp_file_path, encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("Failed to decode the CSV file with available encodings.")

    if 'prompt' not in df.columns:
        raise ValueError("CSV must contain a 'prompt' column")

    documents = [Document(page_content=row['prompt']) for _, row in df.iterrows()]
    vectordb = FAISS.from_documents(documents=documents, embedding=instructor_embeddings)

    vectordb.save_local(vectordb_file_path)
    os.remove(temp_file_path)

def get_qa_chain(api_key):
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from the "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    llm = GooglePalm(google_api_key=api_key, temperature=0.2)

    chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever,
                                        input_key="query", return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain
