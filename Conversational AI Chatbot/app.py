from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables from .env files
load_dotenv()

# Load OpenAI model and get response
def get_openai_response(text):
    openai_llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="text-davinci-003", temperature=0.6)
    response = openai_llm(text)
    return response

# Initialize Streamlit application
st.set_page_config(page_title="Questions and Answers Chatbot", page_icon="🤖")

# Sidebar information
st.sidebar.title("LangChain Q&A Chatbot")
st.sidebar.markdown("""
This app uses **LangChain** and **OpenAI** to generate responses to your questions.  
You can ask any question, and the AI will provide a helpful answer.
""")

# Main title with emoji
st.title("🤖 Questions and Answers Chatbot")

st.header("LangChain Application")

# Input field for user query
input_text = st.text_input("Enter your question", key="input")

# Ensure that a response is generated only if input is provided
response = get_openai_response(input_text) if input_text else "No input provided"

# Button to submit the query
button = st.button("Ask the question")

# Button to clear input field
if st.button("Clear input"):
    st.experimental_rerun()  # Reloads the app to clear the input field

# Display response when the button is clicked
if button:
    st.success("Response generated successfully!")
    st.header("The response is:")
    st.write(response)
