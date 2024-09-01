# Geography Knowledge Chatbot

Welcome to the Geography Knowledge Chatbot! This Streamlit app utilizes Groq AI to answer your geography-related questions and provide insights into geographical facts.

## Project Overview

This project consists of a Streamlit app with two main pages:
- **Home Page**: Provides an introduction to the chatbot and information about the team.
- **Chatbot Page**: Allows users to ask geography-related questions and receive responses from the Groq AI.

## Features

- **Home Page**: 
  - Displays a welcome message.
  - Showcases the team members with their images and IDs.
  - Provides a button to navigate to the chatbot page.

- **Chatbot Page**:
  - Allows users to input geography-related questions.
  - Displays conversation history.
  - Uses Groq AI to generate responses based on user input.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mldatascientist23/Generative_AI_Projects/geography_bot.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd geography-chatbot
    ```

3. **Install dependencies**:
    Make sure you have `pip` installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up secrets**:
    Create a `.streamlit/secrets.toml` file in the root directory and add your Groq API key:
    ```toml
    [default]
    GROQ_API_KEY = "your_groq_api_key_here"
    ```

5. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

- **Home Page**: View the team details and navigate to the chatbot page.
- **Chatbot Page**: Enter your geography-related questions in the input field and press "Submit" to receive answers.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes. Ensure your code follows the project's coding style and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Groq AI**: For providing the AI service used in this project.
- **Streamlit**: For making it easy to create and deploy interactive web apps.

## Contact

For any questions or feedback, please contact:

- **Saad Asghar Ali** - [your-email@example.com](mailto:your-email@example.com)
- **Hamesh Raj** - [hm.raisingani@gmail.com](mailto:your-email@example.com)
- **Mir khalil ur Rehman** - [your-email@example.com](mailto:your-email@example.com)
