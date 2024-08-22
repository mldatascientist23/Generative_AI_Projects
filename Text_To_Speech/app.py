import streamlit as st
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
import torch
from datasets import load_dataset
import soundfile as sf
import io

# Load the processor and model
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

# Load speaker embeddings dataset
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

def generate_speech(text, voice_type):
    inputs = processor(text=text, return_tensors="pt")
    
    # Select speaker embedding based on voice type
    if voice_type == "Male":
        speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
    else:
        speaker_embeddings = torch.tensor(embeddings_dataset[10880]["xvector"]).unsqueeze(0)
    
    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
    
    # Convert speech to bytes
    audio_bytes_io = io.BytesIO()
    sf.write(audio_bytes_io, speech.numpy(), samplerate=16000, format='WAV')
    audio_bytes_io.seek(0)

    return audio_bytes_io

# Streamlit UI
st.markdown(
    """
    <div style="text-align: center;">
        <h2 style="color: #FF5733;">Created by Engr. Hamesh Raj</h2>
        <a href="https://www.linkedin.com/in/datascientisthameshraj/" target="_blank" style="color: #FF5733;">LinkedIn Profile</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🗣️ Text-to-Speech Converter")
st.write("Enter text below, select voice type, and click 'Generate Speech' to convert it to audio.")

# Sidebar for user input
with st.sidebar:
    st.header("Input Options")
    text_input = st.text_area("Text to convert:", "Some example text in the English language")
    voice_type = st.selectbox("Select Voice:", ["Male", "Female"])
    submit_button = st.button("Generate Speech")

# Process the input and generate speech
if submit_button:
    if text_input:
        with st.spinner("Generating speech..."):
            audio_bytes_io = generate_speech(text_input, voice_type)
            st.audio(audio_bytes_io, format="audio/wav")
            st.write("Process completed!")
            
            # Provide a download link for the generated audio
            st.download_button(
                label="Download Audio",
                data=audio_bytes_io,
                file_name="generated_speech.wav",
                mime="audio/wav"
            )
    else:
        st.error("Please enter some text.")
