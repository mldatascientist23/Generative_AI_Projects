import os
from groq import Groq
import gradio as gr
import fitz  # PyMuPDF for PDF text extraction
from PIL import Image
import pytesseract
from fpdf import FPDF  # Library for creating PDFs

# Set your API key
# os.environ['GROQ_API_KEY'] = "YOUR API KEY"

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Initialize the conversation history
conversation_history = []

def extract_text_from_file(uploaded_file):
    text = ""
    try:
        if uploaded_file.name.endswith(".pdf"):
            # Use uploaded_file.name to get the path and open the file using fitz
            doc = fitz.open(uploaded_file.name)
            for page in doc:
                text += page.get_text()
        elif uploaded_file.name.endswith((".png", ".jpg", ".jpeg")):
            image = Image.open(uploaded_file)
            text = pytesseract.image_to_string(image)
        else:
            text = "Unsupported file format. Please upload a PDF or image file."
    except Exception as e:
        text = f"Error extracting text: {str(e)}"
    return text

def legal_chatbot(user_query, uploaded_file):
    role_context = (
        "As a seasoned legal expert with over 30 years of experience specializing in Pakistani law and justice, "
        "your role is to provide precise, actionable, and lawful advice. "
        "You have an in-depth understanding of the Pakistan Penal Code, along with other significant legal frameworks, "
        "and you are well-versed in recent amendments, landmark rulings, "
        "and their implications. You are expected to respond with clear, comprehensive, and contextually accurate legal guidance. "
        "Your response should focus on assisting legal professionals, such as lawyers and judges, in understanding and applying the relevant sections, rules, and case laws. "
        "Ensure that your advice is practical, within the boundaries of law and ethics, and addresses the query with the aim of promoting justice and aiding in the resolution of legal matters. "
        "If the query is unclear or lacks sufficient detail, provide general guidance or ask for additional information to deliver a more tailored response. "
        "Your ultimate goal is to support the legal process and help people achieve justice."
    )

    if uploaded_file:
        file_text = extract_text_from_file(uploaded_file)
        user_query = f"{user_query}\n\nRefer to the following case file content:\n{file_text}"

    llm_input = f"{role_context} {user_query}"
    conversation_history.append({"role": "user", "content": user_query})

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": llm_input}],
            model="llama3-8b-8192",
        )
        response = chat_completion.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": response})
    except Exception as e:
        response = f"An error occurred while generating the response: {str(e)}"
        print(response)  # Log the error for debugging

    return response

def save_conversation():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for message in conversation_history:
        role = "You" if message["role"] == "user" else "Legal AI Assistant"
        pdf.multi_cell(0, 10, f"{role}: {message['content']}\n\n")

    pdf_file = "conversation.pdf"
    pdf.output(pdf_file)

    return pdf_file

def clear_chat():
    global conversation_history
    conversation_history = []
    return ""

css = """
#generate-button {
    background-color: #388E3C;  /* Darker green */
    color: black;
    border-radius: 5px;
    padding: 2px 8px;
    font-size: 16px;  /* Slightly larger font size */
    margin-top: 5px;
    height: 35px;
}

#clear-button {
    background-color: #D32F2F;  /* Darker red */
    color: red;
    border-radius: 5px;
    padding: 2px 8px;
    font-size: 16px;
    margin-top: 5px;
    height: 35px;
}

#save-button {
    background-color: #1976D2;  /* Darker blue */
    color: green;
    border-radius: 5px;
    padding: 2px 8px;
    font-size: 16px;
    margin-top: 5px;
    height: 35px;
}
"""
def gradio_interface():
    with gr.Blocks(css=css) as demo:
        with gr.Row():
            gr.Markdown("<h2 style='text-align: center;'>⚖️ Legal AI Assistant Chatbot</h2>")
        with gr.Row():    
            gr.Markdown("<h4 style='text-align: center;'>Created by: <a href='https://www.linkedin.com/in/datascientisthameshraj/' target='_blank'>Engr. Hamesh Raj</a></h4>")
        with gr.Row():
            gr.Markdown("<h4 style='text-align: center;'>Ask any legal questions related to Pakistani law.</h4>")

        with gr.Row():
            with gr.Column(scale=1, min_width=30):
                uploaded_file = gr.File(label="Upload a case file (PDF or Image)", elem_id="upload-box")
                start_new_button = gr.Button("Start New", elem_id="clear-button", scale=1)
                save_button = gr.Button("Save Conversation", elem_id="save-button", scale=1)

            with gr.Column(scale=2):
                user_query = gr.Textbox(label="Enter your legal query here", placeholder="Ask about any law, section, or legal issue...", lines=3, elem_id="query-box")
                generate_button = gr.Button("Get Legal Advice", elem_id="generate-button", scale=1)
                download_link = gr.File(label="Download PDF", elem_id="download-link", visible=False)

        with gr.Row():
            chat_output = gr.Markdown(elem_id="chat-output")

        def update_chat(user_query, uploaded_file):
            response = legal_chatbot(user_query, uploaded_file)
            chat_history = ""
            for message in reversed(conversation_history):
                role = "You" if message["role"] == "user" else "Legal AI Assistant"
                chat_history += f"**{role}:** {message['content']}\n\n---\n\n"
            return chat_history

        def save_and_update():
            pdf_file = save_conversation()
            return gr.update(visible=True), pdf_file

        generate_button.click(
            fn=update_chat,
            inputs=[user_query, uploaded_file],
            outputs=[chat_output]
        )

        start_new_button.click(
            fn=clear_chat,
            inputs=None,
            outputs=[chat_output]
        )

        save_button.click(
            fn=save_and_update,
            inputs=None,
            outputs=[download_link, download_link]
        )

    demo.launch(share=True)

gradio_interface()