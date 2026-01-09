import streamlit as st
from google import genai

# ✅ Correct: create client with API key
client = genai.Client(api_key="YOUR_API_KEY")

st.title("🤖 Gemini Chatbot")

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Say something..."):
    # show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # ✅ Call Gemini (FREE model)
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    reply = response.text

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    with st.chat_message("assistant"):
        st.markdown(reply)
