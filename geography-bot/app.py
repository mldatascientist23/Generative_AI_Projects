import streamlit as st
import base64
from groq import Groq

# Function to encode the image file
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()  # Return after file is read

# Load the background image
background_image_path = 'assets/map.webp'
background_image = get_base64_of_bin_file(background_image_path)

# Set up common styles for both pages
def set_styles(is_chatbot_page):
    if is_chatbot_page:
        st.markdown(
            """
            <style>
            .stApp {
                background: none;
                height: 100vh;
                color: black;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 2rem;
            }
            .chatbot-title {
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .button-container {
                display: flex;
                justify-content: center;
                width: 100%;
            }
            .button {
                background-color: #2196F3; /* Blue background */
                color: white; /* White text */
                border: 2px solid #2196F3; /* Blue border */
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 18px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 4px;
                width: auto; /* Auto width based on content */
                max-width: 400px; /* Max width for button */
                transition: background-color 0.3s, border-color 0.3s;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                white-space: nowrap; /* Prevent text from wrapping */
                overflow: hidden; /* Hide overflow */
            }
            .button:hover {
                background-color: #1976D2; /* Darker blue */
                border-color: #1976D2; /* Darker blue border */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("data:image/webp;base64,{background_image}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                height: 100vh;
                padding: 2rem;
                color: white;
            }}
            .title {{
                font-size: 48px;
                font-weight: bold;
                text-shadow: 2px 2px 5px black;
                margin-top: 30px;
                text-align: center;
            }}
            .button {{
                background-color: #4CAF50; /* Green background */
                color: white; /* White text */
                border: 2px solid #4CAF50; /* Green border */
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 18px;
                margin-top: 50px;
                cursor: pointer;
                border-radius: 4px;
                width: auto; /* Auto width based on content */
                max-width: 400px; /* Max width for button */
                transition: background-color 0.3s, border-color 0.3s;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                white-space: nowrap; /* Prevent text from wrapping */
                overflow: hidden; /* Hide overflow */
            }}
            .button:hover {{
                background-color: #45a049; /* Darker green */
                border-color: #45a049; /* Darker green border */
            }}
            .contribution {{
                font-size: 20px;
                color: white;
                text-shadow: 1px 1px 3px black;
                margin-top: 50px;
                text-align: center;
            }}
            .contributors {{
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 20px;
                flex-wrap: nowrap; /* Keep items in one line */
                overflow-x: auto; /* Allow horizontal scrolling if needed */
                margin-top: 20px;
                padding: 10px;
            }}
            .contributor {{
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
                flex-shrink: 0; /* Prevent shrinking */
                width: 150px; /* Set a fixed width for each contributor */
            }}
            .contributor img {{
                border-radius: 50%;
                margin-bottom: 5px;
            }}
            .contributor-number {{
                font-size: 18px;
                font-weight: bold;
                color: white;
                margin-bottom: 5px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Initialize Groq client
def initialize_groq_client(api_key):
    return Groq(api_key=api_key)

# Session state to manage page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Define the home page
def home_page():
    set_styles(is_chatbot_page=False)
    
    st.markdown('<div class="title">🌍 Geography Knowledge Chatbot 🌍</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="summary">'
        'Welcome to the Geography Knowledge Chatbot! This app uses Groq AI to answer your geography-related questions. '
        'Explore the bot and get insights into geographical facts.'
        '</div>', unsafe_allow_html=True
    )

    # Define member names and image URLs
    members = [
        {"name": "Saad Asghar Ali - ID: 978", "image": 'assets/saad.jpg'},
        {"name": "Hamesh Raj - ID: 2592", "image": 'assets/raj.jpg'},
        {"name": "Mir khalil ur Rehman - 1145", "image": "https://via.placeholder.com/100"}
    ]

    st.markdown('<div class="contribution">Meet the Team:</div>', unsafe_allow_html=True)
    # Create a row with columns
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            st.image(member["image"], width=100)
            st.write(member["name"])

    # Suggestion with arrow sign above the button
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="font-size: 18px; color: #2196F3;">Click below to go to the Chatbot Page</div>
            <span style="font-size: 24px; color: #2196F3;">👉</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Button to navigate to the chatbot page
    if st.button("Go to Chatbot Page", key="chatbot_button", use_container_width=True):
        st.session_state.page = "chatbot"

# Define the chatbot page
def chatbot_page():
    set_styles(is_chatbot_page=True)
    
    # Get API key from environment variables
    api_key = st.secrets["GROQ_API_KEY"]  # Ensure this is set in .streamlit/secrets.toml
    client = initialize_groq_client(api_key)
    
    st.markdown('<div class="chatbot-title">🗣️ Geography Chatbot 🗣️</div>', unsafe_allow_html=True)
    
    # Display conversation history
    if st.session_state.conversation_history:
        for entry in st.session_state.conversation_history:
            st.write(f"**{entry['role'].capitalize()}:** {entry['content']}")
    
    # Input field
    user_input = st.text_input("Ask a geography question:", "")
    
    # Output area
    if st.button("Submit"):
        if user_input:
            try:
                response = client.chat.completions.create(
                    messages=[
                        {"role": "user", "content": user_input}
                    ],
                    model="gemma-7b-it",
                    max_tokens=150,  # Increase the number of tokens for a more detailed response
                    temperature=0.7,  # Adjust temperature for better coherence
                )
                answer = response.choices[0].message.content
                st.session_state.conversation_history.append({"role": "user", "content": user_input})
                st.session_state.conversation_history.append({"role": "bot", "content": answer})
                st.write(f"**Bot:** {answer}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a question before submitting.")

# Page navigation logic
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "chatbot":
    chatbot_page()
