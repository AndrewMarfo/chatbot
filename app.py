from model import ask_question
import streamlit as st
import time

def stream_response(sentences):
    for word in sentences.split(" "):
        yield word + " "
        time.sleep(0.04)

st.set_page_config(
        page_title="Paul Graham Essay Chatbot",
        
    )

st.title("Welcome to PaulChat 👋")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask Paul any question about the essay 💭")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Generating response..."):
        response = ask_question(prompt)
        # Display AI response in chat message container
        with st.chat_message("assistant"):
            st.write_stream(stream_response(response))

        st.session_state.messages.append({"role": "assistant", "content": response})

