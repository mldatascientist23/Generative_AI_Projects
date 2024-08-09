# Using Streamlit

import google.generativeai as genai
import streamlit as st

# Configure the Google Generative AI API

GOOGLE_API_KEY = "AIzaSyAZXviM7pYcIlnP0CAdasPlN4oA80OT-ds"
genai.configure(api_key=GOOGLE_API_KEY)

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

st.title("Chatbot by using Gemini API")

# Get a user input through a text input box

user_input = st.text_input(f"**Enter your prompt:**", placeholder="write any query here.....")

# Create a button that when clicked, it will generate the response

if st.button("**Submit Query**"):
    if user_input:
        output = getResponseFromModel(user_input)
        st.write(f"**Chatbot Answer:** {output}")
    else:
        st.write("Please enter a prompt.")