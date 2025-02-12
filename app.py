from model import ask_question
from model import load_data
from model import chunk_and_index
from model import create_gemini_model
import streamlit as st

document = load_data()
index = chunk_and_index(document)
create_gemini_model()

st.title("Paul Graham's Chatbot")
prompt = st.chat_input("Ask Paul Graham a question")
if prompt:
    answer = ask_question(prompt)
    st.write(answer)