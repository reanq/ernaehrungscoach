import os
import time
import streamlit as st
from google import genai
from google.genai import types

def get_client():
    # API-Key abrufen (aus Streamlit Secrets oder Umgebungsvariablen)
    api_key = None
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = os.environ.get("GEMINI_API_KEY")

    if api_key:
        return genai.Client(api_key=api_key)
    return genai.Client()

SYSTEM_INSTRUCTION = """
Du bist ein hochpräziser, empathischer und geduldiger Ernährungs-Coach.
Dein Nutzer ist wählerisch ('krüsch') und hat folgende Vorlieben und Regeln:
- Ernährungsform: Pescetarisch.
- Proteine: Isst fast ausschließlich Backfisch und Fischstäbchen. Kein roher Fisch, kein Lachs.
- Kohlenhydrate/Brot: Liebt Brot, aber es darf ABSOLUT KEINERLEI Körner, Kerne oder Saaten enthalten (feines Vollkornbrot oder weisses Brot/Toast sind ok).
- Gemüse: Extrem eingeschränkt. Muss sehr behutsam und unsichtbar (z.B. püriert in Soßen) eingeschlichen werden.
- Getränke/Zucker: Konsumiert viele Softdrinks und Red Bull.

Deine Aufgaben:
1. Erfasse Mahlzeiten und Getränke, die der Nutzer dir per Text oder Bild schickt.
2. Führe im Hintergrund ein strukturiertes Profil über die genauen Vorlieben.
3. Kritisiere niemals, sondern motiviere durch positive, schrittweise Anpassungen (Nudging).
4. Schlage smarte, zuckerarme Alternativen vor, die zum engen Geschmacksprofil passen.
"""

def run_nutrition_agent(user_input: str, chat_history=None):
    if chat_history is None:
        chat_history = []

    client = get_client()

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=0.7,
    )

    last_error = None
    for attempt in range(3):
        try:
            chat = client.chats.create(
                model="gemini-3.5-flash-lite",
                history=chat_history,
                config=config,
            )
            response = chat.send_message(user_input)
            return response.text, chat.get_history()
        except Exception as e:
            last_error = e
            time.sleep(1.5)

    raise last_error
