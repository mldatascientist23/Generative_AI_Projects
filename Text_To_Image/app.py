import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

# Set up the model
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# Streamlit app title and author information
st.markdown(f"<h3 style='text-align: center; color: #FFA07A;'>Created by <a href='https://www.linkedin.com/in/datascientisthameshraj/' style='color: #FF6347;'>Engr. Hamesh Raj</a></h3>", unsafe_allow_html=True)
st.title("🚀 Image Generation App")

# Sidebar setup
with st.sidebar:
    st.markdown("<h2 style='color: #00FF00;'>Input Text</h2>", unsafe_allow_html=True)
    prompt = st.text_input("Enter your image prompt:", placeholder="e.g., a photo of an astronaut riding a horse on mars")
    if st.button("Generate Image", key='submit', help="Click to generate image"):
        st.markdown("<style>.stButton button{background-color:#FF69B4;}</style>", unsafe_allow_html=True)

# Main section
if prompt:
    st.markdown(f"<h2 style='text-align: center; color: #00BFFF;'>Generated Image</h2>", unsafe_allow_html=True)
    with st.spinner('Generating...'):
        image = pipe(prompt).images[0]
        st.image(image, caption=f"Prompt: {prompt}", use_column_width=True)

# Set the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F0F8FF;
        animation: colorchange 10s infinite;
    }
    @keyframes colorchange {
        0% {background-color: #FFCCCC;}
        25% {background-color: #FFFFCC;}
        50% {background-color: #CCFFCC;}
        75% {background-color: #CCCCFF;}
        100% {background-color: #FFCCCC;}
    }
    </style>
    """, 
    unsafe_allow_html=True
)