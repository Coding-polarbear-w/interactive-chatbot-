from dotenv import load_dotenv
load_dotenv()
import streamlit as st 
import google.generativeai as genai 
import os 

genai.configure(api_key=os.getenv("google_api"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question): 
    response = chat.send_message(question, stream = True)
    return response

st.config("Q&A w Shreyansh")
st.header("Conversations with Shreyansh")

if 'chat_history' not in st.session_state: 
    st.session_state['chat_history'] = []

input = st.text_input("input", key="input")
submit = st.button("send")

if input and submit: 
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response: ")
    for chunk in response: 
        st.write(chunk.text)
        st.session_state['chat_history'].apend(("Response", chunk.text))

st.subheader("Chat history: ")

for role, response in st.session_state['chat_hisotry']: 
    st.write(f"{role}: {response}")











if input and submit: 
    response = get_gemini_response(input)
    st.session_state['chat history'].append("")

