# Using Streamlit

import google.generativeai as genai
import streamlit as st

# Configure the Google Generative AI API

# GOOGLE_API_KEY = " "
# genai.configure(api_key=GOOGLE_API_KEY)


# Initialize the Model

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# user_input = input("Enter your prompt: ")
# output = getResponseFromModel(user_input)
# print(output)


# Streamlit UI

st.markdown("##### Created By: **Engr. Hamesh Raj**")
st.markdown("[Contact Here](https://www.linkedin.com/in/datascientisthameshraj)")

st.title(f"**Chatbot by using Gemini API**")

# Sidebar for API key input
st.sidebar.info("The model only gets Google Gemini API key.")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key Here:", type="password", placeholder="Paste your Gemini API Key")

# Get a user input through a text input box

user_input = st.text_input(f"**Enter your prompt:**", placeholder="write any type of queries here.....")

# Create a button that when clicked, it will generate the response

if st.button("**Submit Query**"):
    if api_key and user_input:
        # configure the api key
        genai.configure(api_key=api_key)

        output = getResponseFromModel(user_input)
        st.write(f"**Chatbot Answer:** {output}")
    else:
        st.write("Please enter both the API key and a prompt to generate a response.")