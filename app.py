from model import ask_question
import streamlit as st

st.title("Paul Graham's Chatbot")
prompt = st.chat_input("Ask Paul Graham a question")
if prompt:
    answer = ask_question(prompt)
    st.write(answer)