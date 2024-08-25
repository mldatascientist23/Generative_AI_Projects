# Gradio Audio Transcription and Response App

## Overview

This Gradio app provides an interface to upload an audio file, transcribe the audio using the Whisper model, generate a response using the Groq API, and convert that response to speech. The application features a colorful, gradient background and a user-friendly design.

## Application Link

You can access the live application here: [Gradio Audio Transcription and Response App](https://3e180f171a67076b30.gradio.live/)

## Features

- **Audio Input**: Upload audio files to be processed.
- **Text Response**: Receive a transcribed text response from the audio input.
- **Audio Response**: Get a generated speech response based on the transcribed text.
- **Colorful UI**: Enjoy a visually appealing interface with a gradient background.

## Installation

To run this application locally, follow these steps:

1. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Install ffmpeg**:

    For systems using apt-get (like Debian-based systems), use:

    ```bash
    sudo apt-get install -y ffmpeg
    ```

4. **Set up the Groq API Key**:

    Make sure to set your Groq API key in the environment variable `GROQ_API_KEY`:

    ```bash
    export GROQ_API_KEY=<your-api-key-here>
    ```

## Usage

1. **Upload Audio**: Use the 'Upload your audio file here' section to submit your audio file.
2. **Submit**: Click the 'Submit' button to process the audio.
3. **View Response**: The response text and audio will be displayed on the right side.

## Contact

Created by: [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)