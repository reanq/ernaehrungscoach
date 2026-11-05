import streamlit as st
from agent import run_nutrition_agent
from google.genai import types

st.set_page_config(page_title="Mein Ernährungs-Agent", page_icon="🥗", layout="centered")

st.title("🥗 Mein Ernährungs-Agent")
st.write("Dein persönlicher, geduldiger Coach für deine Ernährung.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Was gab es zu essen oder zu trinken?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    history_for_sdk = []
    for m in st.session_state.messages[:-1]:
        role = "user" if m["role"] == "user" else "model"
        history_for_sdk.append(types.Content(role=role, parts=[types.Part.from_text(text=m["content"])]))

    with st.chat_message("assistant"):
        with st.spinner("Analysiere Mahlzeit..."):
            try:
                response_text, _ = run_nutrition_agent(user_input, history_for_sdk)
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"Fehler: {e}")

