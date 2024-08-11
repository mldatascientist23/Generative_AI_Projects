import streamlit as st
import google.generativeai as genai

# Configure the API key
openai_key = st.secrets["OPENAI_API_KEY"]
genai.configure(api_key=openai_key)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro')

# Function to get a response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text  # Directly access the text attribute

# Streamlit interface

st.set_page_config(page_title="ChatBot by using Gemini API", page_icon=":robot:", layout="centered")


# Add LinkedIn link and powered by:

st.write("Created by: **Engr. Hamesh Raj**")
st.markdown(
    """
    [![Connect on LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-blue)](https://www.linkedin.com/in/datascientisthameshraj/)"""
)

# Title of the Chatbot

st.title("🤖 Gemini API ChatBot 🤖")

# Initialize session state for chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Display chat history with labels
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;">
            <strong>Me:</strong> {user_message}
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div style="
        background-color: #e1ffc7; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;">
            <strong>Chatbot:</strong> {bot_message}
        </p>
    </div>
    """, unsafe_allow_html=True)

# Input field at the bottom, after showing chat history
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Your query: ", "", placeholder="Input your query here...", max_chars=500)
    
    # Add color to the submit button
    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    submit_button = st.form_submit_button("Get Response", use_container_width=True)
    
    if submit_button:
        if user_input:
            # Get the chatbot's response and update history
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
            st.rerun()  # Rerun to immediately update the display
        else:
            st.warning("Please enter your query before submitting.")  # Display warning if input is empty