# E-learning Chatbot

## Udemy Q&A: Question and Answer System Based on Google Palm LLM and Langchain for E-learning Company

This project provides an end-to-end LLM solution using Google Palm and Langchain, specifically tailored for an e-learning company called Udemy. Udemy offers data-related courses and bootcamps, with thousands of learners who use various channels like Discord or email to ask questions. This system aims to deliver a Streamlit-based user interface where students can ask questions and receive answers promptly.

## Project Highlights

- **Live Demo**: [View the demo here](https://question-answer-csv-chatbot.streamlit.app/)

## Features

- Utilizes a real CSV file of FAQs currently used by Udemy.
- Reduces the workload of Udemy's human staff by automating responses.
- Allows students to ask questions directly and receive answers in seconds.

## Learning Outcomes

- **Langchain + Google Palm**: Implementing an LLM-based Q&A system.
- **Streamlit**: Building a user-friendly interface.
- **Huggingface Instructor Embeddings**: Generating text embeddings.
- **FAISS**: Managing vector databases.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/mldatascientist23/Generative_AI_Projects.git

```
2.Navigate to the project directory:


3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
4.Acquire an api key through makersuite.google.com and put it in .env file

```bash
  API_KEY="your_api_key_here"
```
## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser.

- To create a knowledebase of FAQs, click on Create Knolwedge Base button. It will take some time before knowledgebase is created so please wait.

- Once knowledge base is created you will see a directory called faiss_index in your current folder

- Now you are ready to ask questions. Type your question in Question box and hit Enter

## Sample Questions
  - Do you guys provide internship and also do you offer EMI payments?
  - Do you have javascript course?
  - Should I learn power bi or tableau?
  - I've a MAC computer. Can I use powerbi on it?
  - I don't see power pivot. how can I enable it?

## Project Structure

- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- .env: Configuration file for storing your Google API key.