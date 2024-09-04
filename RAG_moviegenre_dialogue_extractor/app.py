import streamlit as st
import pandas as pd
from groq import Groq
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the API key from Streamlit secrets
api_key = st.secrets["GROQ_API_KEY"]

# Initialize the Groq API client with the secret API key
client = Groq(api_key=api_key)

# Streamlit UI
st.title("🎬 Movie Query and Recommendation System 🍿")

# Display creator information
st.markdown("Created by [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)")

# Sidebar for uploading CSV file
st.sidebar.header("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Initialize session state variables
if 'df' not in st.session_state:
    st.session_state.df = None
if 'vector_database' not in st.session_state:
    st.session_state.vector_database = None
if 'model' not in st.session_state:
    st.session_state.model = None

# Input field for user query
user_query = st.text_input("🔍 Enter a movie description or query:")

# Function to process the uploaded file and create the vector database
def process_file(file):
    df = pd.read_csv(file)
    st.session_state.df = df

    # Ensure there are no NaN values in the 'Summary' column
    df['Summary'] = df['Summary'].fillna('')

    # Use 'Summary' for embeddings
    summaries = df['Summary'].tolist()

    # Optimize embedding generation by using smaller model or batching
    st.session_state.model = SentenceTransformer('all-MiniLM-L6-v2')  # Consider using a smaller model for faster processing
    batch_size = 64  # Batch size can be adjusted based on available resources
    summary_embeddings = []

    with st.spinner("Generating embeddings..."):
        for i in range(0, len(summaries), batch_size):
            batch = summaries[i:i+batch_size]
            embeddings = st.session_state.model.encode(batch, show_progress_bar=False)
            summary_embeddings.extend(embeddings)
    
    # Store embeddings in a vector database
    st.session_state.vector_database = np.array(summary_embeddings)

if uploaded_file:
    st.write("File uploaded successfully! Please enter your query to proceed.")

    # Trigger file processing and query handling when the button is pressed
    if st.button("🔎 Get Movie Details"):
        if st.session_state.df is None or st.session_state.vector_database is None:
            with st.spinner("Processing file..."):
                process_file(uploaded_file)

        # Step 4: Retrieve the most similar movie and its details from the vector database
        def retrieve_similar_movie(query, vector_db, top_k=1):
            query_embedding = st.session_state.model.encode([query])
            similarities = cosine_similarity(query_embedding, vector_db)
            top_indices = np.argsort(similarities[0])[::-1][:top_k]
            return st.session_state.df.iloc[top_indices[0]]

        retrieved_movie = retrieve_similar_movie(user_query, st.session_state.vector_database)

        # Prepare the movie details
        title = retrieved_movie['Title']
        year = retrieved_movie['Year']
        rating = retrieved_movie['Rating']
        summary = retrieved_movie['Summary']
        poster_url = retrieved_movie['Movie Poster']
        trailer_url = retrieved_movie['YouTube Trailer']

        # Prepare the message content using the retrieved data
        retrieved_content = f"**Summary:** {summary}\n"
        answer_title = f"**Title:** {title}\n**Year:** {year}\n**Rating:** {rating}\n"

        # Use the retrieved content as context for the chat completion
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer the user's question, but feel free to expand or provide additional information if necessary."},
                {"role": "user", "content": retrieved_content},
                {"role": "user", "content": user_query},
            ],
            model="llama3-8b-8192",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        # Display the generated response
        model_output = chat_completion.choices[0].message.content
        st.write(answer_title)
        st.write(model_output)
        
        if pd.notna(poster_url):
            st.image(poster_url, caption=f"{title} Poster", use_column_width=True)
        
        if pd.notna(trailer_url):
            st.markdown(f"[Watch Trailer]({trailer_url})")
else:
    st.write("Please upload a CSV file to get started.")