import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

# Main page
st.title("📚 🎓 Udemy Chatbot")
st.markdown("**Created by** [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)")

question = st.text_input("💬 Enter your question here: ", placeholder="Ask your question here...")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("📜 Answer")
    st.write(response["result"])