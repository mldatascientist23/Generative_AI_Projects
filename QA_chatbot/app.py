import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

# Initialize session state for 'submit_clicked'
if "submit_clicked" not in st.session_state:
    st.session_state["submit_clicked"] = False

# Main page
st.title("📚 Udemy Chatbot")
st.markdown("**Created by** [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)")

# Question input field
question = st.text_input("💬 Enter your question here:", key="question_input", placeholder="Type your question...")

# Button to submit the question
submit_button = st.button("Submit")

# Handle both the button click and pressing Enter
if submit_button or st.session_state["submit_clicked"]:
    if question:
        st.session_state["submit_clicked"] = True
        try:
            chain = get_qa_chain()
            response = chain({"query": question})

            st.header("📝 Answer")
            st.write(response["result"])
        except Exception as e:
            st.error(f"❌ Error fetching answer: {e}")

        # Reset the session state to allow new submissions
        st.session_state["submit_clicked"] = False