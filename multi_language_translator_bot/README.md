---
title: Multi Language Translator Bot
emoji: ⚡
colorFrom: yellow
colorTo: purple
sdk: streamlit
sdk_version: 1.38.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# 🌐 Multilingual Translator

Created by: [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)

## Overview

This Streamlit application is a multilingual translator that allows users to translate text from English to various languages. It uses the `Helsinki-NLP/opus-mt` models from Hugging Face to perform the translations. The app dynamically loads the appropriate model based on the selected target language and provides real-time translations.

## Features

- **Dynamic Language Selection:** Choose from a wide range of target languages for translation.
- **Real-Time Translation:** Enter text in English and get instant translations in the selected target language.
- **User-Friendly Interface:** Simple and intuitive interface using Streamlit.

## Languages Covered

The application supports translation from English to different languages.
## How to Use

1. **Select Target Language:** Choose the language you want to translate to from the dropdown menu.
2. **Enter Text:** Type or paste the text you want to translate into the text area.
3. **Translate:** Click on the "Translate" button to see the translation in the selected target language.

## Live Demo

Check out the live demo of the app on Hugging Face:

🔗 [Multilingual Translator on Hugging Face](https://huggingface.co/spaces/datascientist22/multi-language-translator-bot)

## Installation

To run the app locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/mldatascientist23/Generative_AI_Projects.git
    cd Generative_AI_Projects/Multilingual_Translator
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Requirements

- `streamlit`
- `transformers`
- `torch`
- 'sentencepiece'

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/datascientisthameshraj/) for any questions or feedback!