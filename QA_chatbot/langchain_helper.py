import os
import pandas as pd
from io import StringIO
from langchain.vectorstores import FAISS
from langchain.llms import GooglePalm
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
import streamlit as st

# Load environment variables
api_key = st.secrets["GOOGLE_API_KEY"]

# Initialize LLM and embeddings
llm = GooglePalm(google_api_key=api_key, temperature=0.2)
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "faiss_index"

def create_vector_db(uploaded_file):
    try:
        # Read the uploaded file content with utf-8 encoding
        uploaded_file.seek(0)
        data = pd.read_csv(uploaded_file, encoding="utf-8")
    except UnicodeDecodeError:
        # If utf-8 fails, try another encoding
        uploaded_file.seek(0)
        data = pd.read_csv(uploaded_file, encoding="ISO-8859-1")  # or 'latin-1'

    # Convert the DataFrame to a list of Document objects
    documents = [Document(page_content=row["prompt"], metadata={"source": row["response"]}) for _, row in data.iterrows()]

    # Create a FAISS vector database
    vectordb = FAISS.from_documents(documents=documents, embedding=instructor_embeddings)

    # Save the vector database locally
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    # Load the vector database
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)

    # Create a retriever
    retriever = vectordb.as_retriever(score_threshold=0.7)

    # Define a prompt template
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer, try to provide as much text as possible from the "response" section in the source document context without making many changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Create a retrieval-based QA chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    return chain