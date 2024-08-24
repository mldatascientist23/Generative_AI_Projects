import streamlit as st
from PIL import Image, UnidentifiedImageError
import requests
from transformers import AutoProcessor, BlipForConditionalGeneration
from io import BytesIO

# Initialize the processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to generate captions
def generate_caption(image, text="A picture of"):
    inputs = processor(images=image, text=text, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)

# Sidebar
st.sidebar.title("🖼️ Upload Image or Paste URL")

# Image upload
uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Image URL input
image_url = st.sidebar.text_input("Or paste Image URL")

# Display uploaded image or image from URL
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
elif image_url:
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content)).convert("RGB")
    except requests.exceptions.HTTPError as e:
        st.sidebar.error(f"Error loading image from URL: {e}")
    except UnidentifiedImageError:
        st.sidebar.error("Error loading image: the URL does not point to a valid image file.")
    except Exception as e:
        st.sidebar.error(f"Error loading image from URL: {e}")


# Header with name and LinkedIn URL
st.markdown("""
    ---
    **Created by [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)**
""")

# Main title and description
st.title("🖼️ Image Captioning with BLIP 🗣️")
st.write("Generate descriptive captions for your images using the BLIP model.")

# Generate button and result display
if st.sidebar.button("Generate"):
    if image:
        caption = generate_caption(image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write(f"**Caption:** {caption}")
    else:
        st.error("Please upload an image or provide a valid image URL.")