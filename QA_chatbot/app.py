import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

# Initialize session state for 'submit_clicked'
if "submit_clicked" not in st.session_state:
    st.session_state["submit_clicked"] = False

st.sidebar.title("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    create_vector_db(uploaded_file)
    st.sidebar.success("File successfully uploaded and vector database created.")

st.title("Question & Answer Chatbot 🧑‍🏫")
st.markdown("**Created by** [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)")

# Question input field
question = st.text_input("Enter your question here:", key="question_input", placeholder="Enter your question here!!!")

# Button to submit the question
submit_button = st.button("Submit")

# Handle both the button click and pressing Enter
if submit_button or st.session_state["submit_clicked"]:
    if question:
        st.session_state["submit_clicked"] = True
        chain = get_qa_chain()
        response = chain({"query": question})

        st.header("Answer")
        st.write(response["result"])

        # Reset the session state to allow new submissions
        st.session_state["submit_clicked"] = False
