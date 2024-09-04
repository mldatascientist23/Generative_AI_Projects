---
title: Rag Moviegenre Dialogue
emoji: 🦀
colorFrom: red
colorTo: yellow
sdk: streamlit
sdk_version: 1.38.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
# 🎬 Movie Query and Recommendation System 🍿

This Streamlit app allows users to query and get recommendations for movies based on a provided description. The app uses a pre-uploaded CSV file containing movie details, generates embeddings for the movie summaries, and retrieves the most relevant movie based on user input using cosine similarity. The application also provides additional context using the Groq API.

## Features

- **Upload CSV File:** Upload a CSV file with movie details, including columns like `Title`, `Year`, `Rating`, `Summary`, `Movie Poster`, and `YouTube Trailer`.
- **Movie Query:** Enter a description or query related to a movie, and the app will return the most similar movie from the database.
- **Movie Details:** Get detailed information about the retrieved movie, including the title, year, rating, summary, movie poster, and a link to the YouTube trailer.
- **Integration with Groq API:** Uses the Groq API to provide additional context and insights based on the retrieved movie details.

## Installation and Usage

To run this application locally, follow these steps:

1. **Clone the Repository:**
   - Open your terminal and run:
     ```bash
     git clone https://github.com/mldatascientist23/Generative_AI_Projects.git
     cd Generative_AI_Projects
     ```

2. **Create a `requirements.txt` File:**
   - Inside the project directory, create a `requirements.txt` file with the following content:
     ```bash
     streamlit
     pandas
     sentence-transformers
     scikit-learn
     numpy
     groq
     ```

3. **Install the Dependencies:**
   - Run the following command to install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Set Up Streamlit Secrets:**
   - In your Streamlit app directory, create a `.streamlit` directory.
   - Inside the `.streamlit` directory, create a `secrets.toml` file.
   - Add your Groq API key to the `secrets.toml` file like this:
     ```toml
     GROQ_API_KEY = "your_groq_api_key_here"
     ```

5. **Run the Streamlit App:**
   - Start the app by running:
     ```bash
     streamlit run movie_query_app.py
     ```

6. **Use the App:**
   - **Upload a CSV File:** Use the sidebar to upload your CSV file containing movie details.
   - **Query a Movie:** Enter a description or a query in the input field and click the "Get Movie Details" button.
   - **View Results:** The app will display the most similar movie based on your query, including the title, year, rating, summary, movie poster, and a link to the YouTube trailer.

## Created by

[Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)