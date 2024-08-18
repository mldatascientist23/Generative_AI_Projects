import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint  # Updated import

# Retrieve Hugging Face API token from Streamlit secrets
huggingface_api_token = st.secrets["HUGGINGFACE_API_KEY"]

# Initialize the HuggingFaceEndpoint model
repo_id = "openai-community/gpt2"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    huggingfacehub_api_token=huggingface_api_token,
    max_length=128,    # Explicitly passing max_length
    temperature=0.7    # Explicitly passing temperature
)

# Streamlit interface with emojis
st.title("🤖 Chatbot with GPT-2 🤖")
st.write("This chatbot is powered by a GPT-2 model hosted on Hugging Face.")

user_input = st.text_input("💬 You:", placeholder="Type your message here...")

if st.button("🚀 Submit"):
    if user_input:
        try:
            # Use invoke() instead of calling llm directly
            response = llm.invoke(user_input)
            st.write(f"🤖 Chatbot: {response}")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
    else:
        st.write("❗ Please enter a message.")