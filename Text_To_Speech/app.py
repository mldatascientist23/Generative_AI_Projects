import streamlit as st
from transformers import pipeline
import torch
import soundfile as sf
from datasets import load_dataset
import io

# Set up the text-to-speech pipeline
synthesizer = pipeline("text-to-speech", model="microsoft/speecht5_tts")
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

# Define the voice options and their corresponding speaker embeddings
voice_options = {
    "Male": torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0),
    "Female": torch.tensor(embeddings_dataset[7300]["xvector"]).unsqueeze(0),
}

# Streamlit UI
st.set_page_config(page_title="🗣️ Text-to-Speech Converter", layout="wide")

# Add colored header with LinkedIn link above the main title
st.markdown(
    """
    <style>
    .header {
        font-size: 16px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        margin-top: 20px;
    }
    .header a {
        color: #28B463;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="header">Created by <a href="https://www.linkedin.com/in/datascientisthameshraj/" target="_blank">Engr. Hamesh Raj</a></div>',
    unsafe_allow_html=True
)

# Main title
st.title("🗣️ Text-to-Speech Converter")

# Sidebar for text input with placeholder
st.sidebar.title("Input Text")
text_input = st.sidebar.text_area("Enter text here:", placeholder="Type something to convert to speech...")

# Voice selection dropdown
voice_choice = st.sidebar.selectbox("Select Voice:", options=list(voice_options.keys()))

# Button to generate speech
if st.sidebar.button("Generate Speech"):
    if not text_input.strip():
        st.sidebar.error("⚠️ Please enter some text to convert to speech!")
    else:
        st.write("Processing...")
        speaker_embedding = voice_options[voice_choice]
        speech = synthesizer(text_input, speaker_embeddings=speaker_embedding)

        # Convert the waveform to bytes
        audio_bytes_io = io.BytesIO()
        sf.write(audio_bytes_io, speech["audio"], samplerate=speech["sampling_rate"], format='WAV')
        audio_bytes_io.seek(0)

        st.write("Processing has been completed!")
        st.subheader("🎧 Resulting Audio")
        st.audio(audio_bytes_io, format="audio/wav")

        # Add download button
        st.download_button(
            label="⬇️ Download Audio",
            data=audio_bytes_io,
            file_name="speech.wav",
            mime="audio/wav"
        )
