import streamlit as st
import re
import os
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import bs4
import torch
from transformers import pipeline

# Define the embedding class
class SentenceTransformerEmbedding:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        embeddings = self.model.encode(texts, convert_to_tensor=True)
        if isinstance(embeddings, torch.Tensor):
            return embeddings.cpu().detach().numpy().tolist()  # Convert tensor to list
        return embeddings

    def embed_query(self, query):
        embedding = self.model.encode([query], convert_to_tensor=True)
        if isinstance(embedding, torch.Tensor):
            return embedding.cpu().detach().numpy().tolist()[0]  # Convert tensor to list
        return embedding[0]

# Streamlit UI setup
st.title("🤖 Chatbot with URL-based Document Retrieval")

# Sidebar Style with Multicolored Background
sidebar_bg_style = """
    <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #ffafbd, #ffc3a0, #2193b0, #6dd5ed);
        }
    </style>
"""
st.markdown(sidebar_bg_style, unsafe_allow_html=True)

# Main Content Style with Multicolored Background
main_bg_style = """
    <style>
        .main .block-container {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
            padding: 2rem;
        }
        .css-18e3th9 {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
        }
    </style>
"""
st.markdown(main_bg_style, unsafe_allow_html=True)

# Sidebar: Input for URL and API keys
st.sidebar.title("Settings")

# Input field for entering URL dynamically with placeholder and help text
url_input = st.sidebar.text_input("Enter Blog Post URL", placeholder="e.g., https://example.com/blog", help="Paste the full URL of the blog post you want to retrieve data from")

# Validate the URL and show a success message when correct
if url_input:
    if re.match(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", url_input):
        st.sidebar.markdown('<p style="color:green; font-weight:bold;">URL is correctly entered</p>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown('<p style="color:red; font-weight:bold;">Invalid URL, please enter a valid one</p>', unsafe_allow_html=True)

# Option to use pre-provided API keys
use_preprovided_keys = st.sidebar.checkbox("Use pre-provided API keys")

# Input fields for API keys with placeholders and helper text
if not use_preprovided_keys:
    api_key_1 = st.sidebar.text_input("Enter LangChain API Key", type="password", placeholder="Enter your LangChain API Key", help="Please enter a valid LangChain API key here")
    api_key_2 = st.sidebar.text_input("Enter Groq API Key", type="password", placeholder="Enter your Groq API Key", help="Please enter your Groq API key here")
else:
    api_key_1 = "your-preprovided-langchain-api-key"  # Replace with your actual pre-provided key
    api_key_2 = "your-preprovided-groq-api-key"  # Replace with your actual pre-provided key
    st.sidebar.markdown('<p style="color:blue; font-weight:bold;">Using pre-provided API keys</p>', unsafe_allow_html=True)

# Submit button for API keys with a success/warning message
if st.sidebar.button("Submit API Keys"):
    if use_preprovided_keys or (api_key_1 and api_key_2):
        os.environ["LANGCHAIN_API_KEY"] = api_key_1
        os.environ["GROQ_API_KEY"] = api_key_2
        st.sidebar.markdown('<p style="color:green; font-weight:bold;">API keys are set</p>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown('<p style="color:red; font-weight:bold;">Please fill in both API keys or select the option to use pre-provided keys</p>', unsafe_allow_html=True)

# Marquee effect with bold, stylish text and a LinkedIn link
st.markdown("""
    <marquee behavior="scroll" direction="left" scrollamount="10">
        <p style='font-size:24px; color:#FF5733; font-weight:bold;'>
            Created by: <a href="https://www.linkedin.com/in/datascientisthameshraj/" target="_blank" style="color:#1E90FF; text-decoration:none;">Engr. Hamesh Raj</a>
        </p>
    </marquee>
    """, unsafe_allow_html=True)

# Title of the chatbot
st.markdown('<h1 style="color:#4CAF50; font-weight:bold;">🤖 Chatbot with URL-based Document Retrieval</h1>', unsafe_allow_html=True)

# Chat query input field with placeholder and help text
query = st.text_input("Ask a question based on the blog post", placeholder="Type your question here...", help="Enter a question related to the content of the blog post")

# Placeholder to display responses
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# CustomLanguageModel class with summarization
class CustomLanguageModel:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # Replace with desired model

    def generate(self, prompt, context):
        summary = self.summarize_context(context)
        return f"Generated response: '{prompt}'. Summary: '{summary}'."

    def summarize_context(self, context):
        summarized = self.summarizer(context, max_length=200, min_length=100, do_sample=False)
        return summarized[0]['summary_text']  # Ensure it outputs full, meaningful sentences

# Define a callable class for RAGPrompt
class RAGPrompt:
    def __call__(self, data):
        return {"question": data["question"], "context": data["context"]}

# Submit button for chat
if st.button("Submit Query"):
    if not query:
        st.warning("Please enter a query before submitting!")
    elif not url_input:
        st.warning("Please enter a valid URL in the sidebar.")
    else:
        try:
            # Blog loading logic based on user input URL
            loader = WebBaseLoader(
                web_paths=(url_input,),  # Use the user-input URL
                bs_kwargs=dict(
                    parse_only=bs4.SoupStrainer()  # Adjust based on the user's URL structure
                ),
            )
            docs = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=300)
            splits = text_splitter.split_documents(docs)

            # Initialize the embedding model
            embedding_model = SentenceTransformerEmbedding('all-MiniLM-L6-v2')

            # Initialize Chroma with the embedding class
            vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_model)

            # Retrieve and generate using the relevant snippets of the blog
            retriever = vectorstore.as_retriever()

            # Retrieve relevant documents
            retrieved_docs = retriever.get_relevant_documents(query)

            # Format the retrieved documents
            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            context = format_docs(retrieved_docs)

            # Initialize the language model
            custom_llm = CustomLanguageModel()

            # Initialize RAG chain using the prompt
            prompt = RAGPrompt()

            # Apply the prompt directly to the data (no chaining using `|`)
            prompt_data = prompt({"question": query, "context": context})

            # Generate the response using the language model, focusing on the answer from the retrieved context
            result = custom_llm.generate(prompt_data["question"], prompt_data["context"])

            # Store query and response in session for chat history
            st.session_state['chat_history'].append((query, result))
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display chat history
for q, r in st.session_state['chat_history']:
    st.write(f"**User:** {q}")
    st.write(f"**Bot:** {r}")