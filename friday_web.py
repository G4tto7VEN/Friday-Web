import streamlit as st
from duckduckgo_search import DDGS
import time

# --- PAGE CONFIG (Makes it look like an App) ---
st.set_page_config(page_title="F.R.I.D.A.Y. AI", page_icon="🤖")

# --- CUSTOM STYLING (Blue & Black Theme) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00BFFF; }
    .stTextInput > div > div > input { background-color: #111; color: #00BFFF; border: 2px solid #00BFFF; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 F.R.I.D.A.Y.")
st.write("Future Ready Intelligent Device Activating You")

# --- THE BRAIN ---
def web_search(query):
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=1)]
            if results:
                return results[0]['body']
            return "I couldn't find anything on that, Kenny."
    except:
        return "Connection error. Is the internet working?"

# --- CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chats
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask Friday..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Show Friday's answer
    with st.chat_message("assistant"):
        response = web_search(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})