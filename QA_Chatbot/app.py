import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain

# Streamlit Sidebar
st.sidebar.title("FAQ Q&A Chatbot 🧑‍🏫")
csv_file = st.sidebar.file_uploader("📄 Upload FAQ CSV File", type=["csv"])

if csv_file:
    if st.sidebar.button("📥 Create Knowledgebase"):
        create_vector_db(csv_file)
        st.sidebar.success("Knowledgebase created successfully!")

# Main Interface
st.title("FAQ Q&A Chatbot")
st.markdown("Created by [**Engr. Hamesh Raj**](https://www.linkedin.com/in/datascientisthameshraj/)")

question = st.text_input("🤔 Ask a Question: ", placeholder="Type your question here... 💬")

if st.button("🔍 Query"):
    if question.strip() == "":
        st.warning("⚠️ Please enter a question before submitting!")
    else:
        api_key = st.secrets["GOOGLE_API_KEY"]
        chain = get_qa_chain(api_key)
        response = chain(question)
        st.header("📝 Answer")
        st.write(response["result"])
