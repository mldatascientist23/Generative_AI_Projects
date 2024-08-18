import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain

# Streamlit Sidebar
st.sidebar.title("FAQ Q&A Chatbot 🧑‍🏫")

# File uploader for CSV file
csv_file = st.sidebar.file_uploader("📄 Upload FAQ CSV File", type=["csv"])

if csv_file:
    # Button to create the vector database
    if st.sidebar.button("📥 Create Knowledgebase"):
        create_vector_db(csv_file)
        st.sidebar.success("Knowledgebase created successfully!")

# Main Interface
st.title("FAQ Q&A Chatbot")
st.markdown("Created by [**Engr. Hamesh Raj**](https://www.linkedin.com/in/datascientisthameshraj/)")

# Input field for the question with a placeholder
question = st.text_input("🤔 Ask a Question: ", placeholder="Type your question here... 💬")

# Submit button
if st.button("🔍 Query"):
    if question.strip() == "":
        st.warning("⚠️ Please enter a question before submitting!")
    else:
        chain = get_qa_chain()
        response = chain(question)
        st.header("📝 Answer")
        st.write(response["result"])