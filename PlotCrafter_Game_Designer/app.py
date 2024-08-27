import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API keys
claude_api_key = os.getenv("ANTHROPIC_API_KEY")

# Initialize Claude AI client
client = anthropic.Anthropic(api_key=claude_api_key)

# Function to generate text using Claude AI
def generate_text(prompt, model_name="claude-3-opus-20240229"):
    response = client.messages.create(
        model=model_name,
        max_tokens=500,
        temperature=0.5,
        system=f"You are a creative writer. Based on the following description, generate content for a game design document: {prompt}",
        messages=[
            {"role": "user", "content": [{"type": "text", "text": prompt}]}
        ]
    )
    return response.content[0].text

# Main Function
def main():
    st.set_page_config(page_title="PlotCrafter", layout="wide")
    
    # Custom CSS for colorful backgrounds and title
    st.markdown("""
        <style>
            .reportview-container {
                background: linear-gradient(90deg, #FFDEE9 0%, #B5FFFC 100%);
                padding: 10px;
            }
            .sidebar .sidebar-content {
                background: linear-gradient(90deg, #FFF5BA 0%, #FFE4E1 100%);
            }
            .title {
                font-size: 3rem;
                color: #FFA07A;
                text-align: center;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .created-by {
                font-size: 1rem;
                color: #008080;
                text-align: center;
                margin-bottom: 20px;
            }
            .description {
                font-size: 1.5rem;
                color: #555;
                text-align: center;
                margin: 20px 0;
                padding: 0 50px;
                line-height: 1.5;
            }
        </style>
    """, unsafe_allow_html=True)

    # Display your name and LinkedIn link
    st.markdown('<div class="created-by">Created by: <a href="https://www.linkedin.com/in/datascientisthameshraj/" target="_blank">Engr. Hamesh Raj</a></div>', unsafe_allow_html=True)
    
    # App title
    st.markdown('<div class="title">🛠️ PlotCrafter</div>', unsafe_allow_html=True)
    
    # Title description stretched across the page
    st.markdown('<div class="description">*PlotCrafter* is a cutting-edge AI app designed to empower *game developers* and creators. With PlotCrafter, you can effortlessly craft captivating game design documents. From crafting immersive storylines and intricate plots to defining compelling protagonists and antagonists, PlotCrafter unlocks your creative potential and streamlines the game design process.</div>', unsafe_allow_html=True)
    
    # Sidebar for user input
    with st.sidebar:
        st.header("Controls")
        image_description = st.text_area(
            "Set the foundation for the game world by providing a detailed and imaginative description of the overall theme, setting, and gameplay elements.",
            placeholder="e.g., A futuristic city where technology and magic coexist...",
            height=100
        )
        protagonist_description = st.text_area(
            "Introduce the main character of the game. Describe their appearance, personality, strengths, and weaknesses. What makes them unique and interesting?",
            placeholder="e.g., A cybernetic detective with a dark past...",
            height=100
        )
        antagonist_description = st.text_area(
            "Describe the primary antagonist or enemy in the game. What are their motivations, abilities, and characteristics? How do they pose a challenge to the protagonist?",
            placeholder="e.g., An AI overlord seeking to eliminate all organic life...",
            height=100
        )

        generate_text_btn = st.button("Generate Game Design")

    # Two columns for other content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Game Environment")
        if generate_text_btn and image_description:
            with st.spinner("Generating game environment description..."):
                generated_environment = generate_text(f"Generate a detailed description of a game environment based on this theme and setting: {image_description}")
                st.markdown(generated_environment)

        st.subheader("Antagonist")
        if generate_text_btn and antagonist_description:
            with st.spinner("Generating antagonist description..."):
                generated_antagonist = generate_text(f"Generate a detailed description of a game antagonist based on this description: {antagonist_description}")
                st.markdown(generated_antagonist)

    with col2:
        st.subheader("Story")
        if generate_text_btn and image_description:
            with st.spinner("Generating game story..."):
                generated_story = generate_text(f"Create a creative and engaging game story that includes a protagonist, antagonist, and a challenge based on this description: {image_description}")
                st.markdown(generated_story)

        st.subheader("Protagonist")
        if generate_text_btn and protagonist_description:
            with st.spinner("Generating protagonist description..."):
                generated_protagonist = generate_text(f"Generate a detailed description of a game protagonist based on this description: {protagonist_description}")
                st.markdown(generated_protagonist)

        st.subheader("Game Plot")
        if generate_text_btn and image_description:
            with st.spinner("Generating game plot..."):
                generated_plot = generate_text(f"Generate a short game plot with a hook, gameplay relation, sticky mechanics, and setting based on this description: {image_description}")
                st.markdown(generated_plot)

# Run Main Function 
if __name__ == "__main__":
    main()