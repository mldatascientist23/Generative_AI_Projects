import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Define a dictionary to map language names to model identifiers
models = {
    'Afrikaans': 'Helsinki-NLP/opus-mt-en-af',
    'Amharic': 'Helsinki-NLP/opus-mt-en-am',
    'Arabic': 'Helsinki-NLP/opus-mt-en-ar',
    'Asturian': 'Helsinki-NLP/opus-mt-en-ast',
    'Azerbaijani': 'Helsinki-NLP/opus-mt-en-az',
    'Bashkir': 'Helsinki-NLP/opus-mt-en-ba',
    'Belarusian': 'Helsinki-NLP/opus-mt-en-be',
    'Bulgarian': 'Helsinki-NLP/opus-mt-en-bg',
    'Bengali': 'Helsinki-NLP/opus-mt-en-bn',
    'Breton': 'Helsinki-NLP/opus-mt-en-br',
    'Bosnian': 'Helsinki-NLP/opus-mt-en-bs',
    'Catalan': 'Helsinki-NLP/opus-mt-en-ca',
    'Cebuano': 'Helsinki-NLP/opus-mt-en-ceb',
    'Czech': 'Helsinki-NLP/opus-mt-en-cs',
    'Welsh': 'Helsinki-NLP/opus-mt-en-cy',
    'Danish': 'Helsinki-NLP/opus-mt-en-da',
    'German': 'Helsinki-NLP/opus-mt-en-de',
    'Greek': 'Helsinki-NLP/opus-mt-en-el',
    'English': 'Helsinki-NLP/opus-mt-en-en',
    'Spanish': 'Helsinki-NLP/opus-mt-en-es',
    'Estonian': 'Helsinki-NLP/opus-mt-en-et',
    'Persian': 'Helsinki-NLP/opus-mt-en-fa',
    'Fulah': 'Helsinki-NLP/opus-mt-en-ff',
    'Finnish': 'Helsinki-NLP/opus-mt-en-fi',
    'French': 'Helsinki-NLP/opus-mt-en-fr',
    'Western Frisian': 'Helsinki-NLP/opus-mt-en-fy',
    'Irish': 'Helsinki-NLP/opus-mt-en-ga',
    'Scottish Gaelic': 'Helsinki-NLP/opus-mt-en-gd',
    'Galician': 'Helsinki-NLP/opus-mt-en-gl',
    'Gujarati': 'Helsinki-NLP/opus-mt-en-gu',
    'Hausa': 'Helsinki-NLP/opus-mt-en-ha',
    'Hebrew': 'Helsinki-NLP/opus-mt-en-he',
    'Hindi': 'Helsinki-NLP/opus-mt-en-hi',
    'Croatian': 'Helsinki-NLP/opus-mt-en-hr',
    'Haitian Creole': 'Helsinki-NLP/opus-mt-en-ht',
    'Hungarian': 'Helsinki-NLP/opus-mt-en-hu',
    'Armenian': 'Helsinki-NLP/opus-mt-en-hy',
    'Indonesian': 'Helsinki-NLP/opus-mt-en-id',
    'Igbo': 'Helsinki-NLP/opus-mt-en-ig',
    'Iloko': 'Helsinki-NLP/opus-mt-en-ilo',
    'Icelandic': 'Helsinki-NLP/opus-mt-en-is',
    'Italian': 'Helsinki-NLP/opus-mt-en-it',
    'Japanese': 'Helsinki-NLP/opus-mt-en-ja',
    'Javanese': 'Helsinki-NLP/opus-mt-en-jv',
    'Georgian': 'Helsinki-NLP/opus-mt-en-ka',
    'Kazakh': 'Helsinki-NLP/opus-mt-en-kk',
    'Central Khmer': 'Helsinki-NLP/opus-mt-en-km',
    'Kannada': 'Helsinki-NLP/opus-mt-en-kn',
    'Korean': 'Helsinki-NLP/opus-mt-en-ko',
    'Luxembourgish': 'Helsinki-NLP/opus-mt-en-lb',
    'Ganda': 'Helsinki-NLP/opus-mt-en-lg',
    'Lingala': 'Helsinki-NLP/opus-mt-en-ln',
    'Lao': 'Helsinki-NLP/opus-mt-en-lo',
    'Lithuanian': 'Helsinki-NLP/opus-mt-en-lt',
    'Latvian': 'Helsinki-NLP/opus-mt-en-lv',
    'Malagasy': 'Helsinki-NLP/opus-mt-en-mg',
    'Macedonian': 'Helsinki-NLP/opus-mt-en-mk',
    'Malayalam': 'Helsinki-NLP/opus-mt-en-ml',
    'Mongolian': 'Helsinki-NLP/opus-mt-en-mn',
    'Marathi': 'Helsinki-NLP/opus-mt-en-mr',
    'Malay': 'Helsinki-NLP/opus-mt-en-ms',
    'Burmese': 'Helsinki-NLP/opus-mt-en-my',
    'Nepali': 'Helsinki-NLP/opus-mt-en-ne',
    'Dutch': 'Helsinki-NLP/opus-mt-en-nl',
    'Norwegian': 'Helsinki-NLP/opus-mt-en-no',
    'Northern Sotho': 'Helsinki-NLP/opus-mt-en-ns',
    'Occitan': 'Helsinki-NLP/opus-mt-en-oc',
    'Oriya': 'Helsinki-NLP/opus-mt-en-or',
    'Panjabi': 'Helsinki-NLP/opus-mt-en-pa',
    'Polish': 'Helsinki-NLP/opus-mt-en-pl',
    'Pushto': 'Helsinki-NLP/opus-mt-en-ps',
    'Portuguese': 'Helsinki-NLP/opus-mt-en-pt',
    'Romanian': 'Helsinki-NLP/opus-mt-en-ro',
    'Russian': 'Helsinki-NLP/opus-mt-en-ru',
    'Sindhi': 'Helsinki-NLP/opus-mt-en-sd',
    'Sinhala': 'Helsinki-NLP/opus-mt-en-si',
    'Slovak': 'Helsinki-NLP/opus-mt-en-sk',
    'Slovenian': 'Helsinki-NLP/opus-mt-en-sl',
    'Somali': 'Helsinki-NLP/opus-mt-en-so',
    'Albanian': 'Helsinki-NLP/opus-mt-en-sq',
    'Serbian': 'Helsinki-NLP/opus-mt-en-sr',
    'Swati': 'Helsinki-NLP/opus-mt-en-ss',
    'Sundanese': 'Helsinki-NLP/opus-mt-en-su',
    'Swedish': 'Helsinki-NLP/opus-mt-en-sv',
    'Swahili': 'Helsinki-NLP/opus-mt-en-sw',
    'Tamil': 'Helsinki-NLP/opus-mt-en-ta',
    'Thai': 'Helsinki-NLP/opus-mt-en-th',
    'Tagalog': 'Helsinki-NLP/opus-mt-en-tl',
    'Tswana': 'Helsinki-NLP/opus-mt-en-tn',
    'Turkish': 'Helsinki-NLP/opus-mt-en-tr',
    'Ukrainian': 'Helsinki-NLP/opus-mt-en-uk',
    'Urdu': 'Helsinki-NLP/opus-mt-en-ur',
    'Uzbek': 'Helsinki-NLP/opus-mt-en-uz',
    'Vietnamese': 'Helsinki-NLP/opus-mt-en-vi',
    'Wolof': 'Helsinki-NLP/opus-mt-en-wo',
    'Xhosa': 'Helsinki-NLP/opus-mt-en-xh',
    'Yiddish': 'Helsinki-NLP/opus-mt-en-yi',
    'Yoruba': 'Helsinki-NLP/opus-mt-en-yo',
    'Chinese': 'Helsinki-NLP/opus-mt-en-zh',
    'Zulu': 'Helsinki-NLP/opus-mt-en-zu'
}

def load_model(language):
    """Load the model and tokenizer for the specified target language."""
    model_name = models.get(language)
    if model_name:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        return model, tokenizer
    else:
        st.error(f"Model for {language} not found.")
        return None, None

def translate_text(text, model, tokenizer):
    """Translate text using the provided model and tokenizer."""
    inputs = tokenizer.encode(text, return_tensors="pt")
    translated = model.generate(inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

def main():
    st.title("🌐 Multilingual Translator")
    st.markdown("Created by: [**Engr. Hamesh Raj**](https://www.linkedin.com/in/datascientisthameshraj/)")

    # Target language selection
    target_language = st.selectbox("Select target language:", list(models.keys()))

    # Input text area
    text_to_translate = st.text_area("Enter text in English:")

    if st.button("Translate"):
        if text_to_translate:
            # Load the model based on target language
            model, tokenizer = load_model(target_language)
            
            if model and tokenizer:
                translated_text = translate_text(text_to_translate, model, tokenizer)
                st.write(f"**Translation in {target_language}:**")
                st.write(translated_text)
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()