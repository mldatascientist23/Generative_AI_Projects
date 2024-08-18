
# E-learning-Chatbot

## FAQ Q&A: Question and Answer System Based on Google Palm LLM and Langchain

This project is an end-to-end LLM-based Q&A system using Google Palm and Langchain, designed for an e-learning platform. The chatbot provides a Streamlit-based user interface where students can upload a CSV file of FAQs, create a knowledge base, and ask questions to receive instant answers.

## Project Highlights
- **Live Demo:** [Link to Streamlit App](https://https://question-answer-csv-chatbot.streamlit.app//)
- **Use Case:** The system uses a real CSV file of FAQs to assist users. The LLM-based Q&A system reduces the workload of human staff by answering questions automatically.
- **Technology Stack:** 
  - Langchain + Google Palm for LLM-based Q&A
  - Streamlit for UI
  - Huggingface Instructor Embeddings for text embeddings
  - FAISS for vector database creation

## Learning Outcomes
- Implement LLM-based Q&A systems with Langchain and Google Palm
- Build user interfaces using Streamlit
- Utilize Huggingface Instructor Embeddings for text processing
- Work with FAISS for creating and querying vector databases

## Installation

1. Clone this repository to your local machine using:

   \`\`\`bash
   git clone https://github.com/mldatascientist23/Generative_AI_Projects.git
   \`\`\`

2. Navigate to the project directory:

   \`\`\`bash
   cd elearning-chatbot
   \`\`\`

3. Install the required dependencies using pip:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. Acquire an API key through [makersuite.google.com](https://makersuite.google.com/) and put it in a `.env` file:

   \`\`\`bash
   API_KEY="your_api_key_here"
   \`\`\`

## Usage

1. Run the Streamlit app by executing:

   \`\`\`bash
   streamlit run main.py
   \`\`\`

2. The web app will open in your browser.

- To create a knowledge base of FAQs, click on the "Create Knowledgebase" button. This process may take some time, so please wait patiently.
- Once the knowledge base is created, you will see a directory called `faiss_index` in your current folder.
- Now you are ready to ask questions. Type your question in the "Question" box and hit Enter.

## Sample Questions
- What courses do you offer related to data science?
- Can I get a certificate for completing the bootcamp?
- Are your courses accessible for beginners?
- How do I access course materials on my mobile device?
- What payment methods do you accept?

## Project Structure

- `app.py`: The main Streamlit application script.
- `langchain_helper.py`: Contains all the Langchain-related code.
- `requirements.txt`: A list of required Python packages for the project.
- `.env`: Configuration file for storing your Google API key.
- `.streamlit/config.toml`: Configuration file for storing your Google API key and Streamlit settings.- 