---
title: BlogpostQA Retrieval Bot
emoji: ⚡
colorFrom: purple
colorTo: pink
sdk: streamlit
sdk_version: 1.38.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# 🤖 Chatbot with URL-based Document Retrieval

This Streamlit app is designed to provide a chatbot interface for querying content from a blog post URL. It utilizes various NLP models to retrieve and summarize relevant content based on user queries.

## Features

- **URL Input**: Allows users to input the URL of a blog post.
- **API Key Input**: Users can either use pre-provided API keys or enter their own.
- **Chat Interface**: Users can ask questions related to the content of the blog post.
- **Dynamic Styling**: Includes colorful, animated backgrounds and a stylish sidebar.
- **Response Generation**: Uses models to retrieve and summarize content related to the query.

## Installation

To run this app, ensure you have Python installed, then install the necessary packages using the provided `requirements.txt` file.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mldatascientist23/Generative_AI_Projects.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd your-repository
    ```

3. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: .\env\Scripts\activate
    ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Access the app**:
    Open a web browser and navigate to `https://huggingface.co/spaces/datascientist22/blogpostQA-retrieval-bot` to interact with the chatbot.

### Sidebar Configuration

- **Enter Blog Post URL**: Input the URL of the blog post you want to retrieve data from.
- **Use pre-provided API keys**: Check this box if you want to use pre-provided API keys. If unchecked, enter your own API keys.
- **API Key Fields**: Enter your LangChain and Groq API keys if not using pre-provided keys.

### Main Interface

- **Ask a question based on the blog post**: Type your question in the input field and click "Submit Query" to get a response based on the content of the blog post.

## Error Handling

- **URL Validation**: Ensure that the URL is valid before submitting.
- **API Key Submission**: Both API keys must be provided unless using pre-provided keys.

## Notes

- Ensure that the `requirements.txt` file includes the necessary libraries, such as `streamlit`, `langchain`, `langchain_chroma`, `langchain_community`, `langchain_core`, `langchain_text_splitters`, `sentence_transformers`, `torch`, and `transformers`.
- The app uses the `facebook/bart-large-cnn` model for summarization, and `SentenceTransformer` for embedding.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **Created by [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)**

Feel free to open an issue or submit a pull request if you have any questions or suggestions!
