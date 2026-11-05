# 🥗 Mein Ernährungs-Agent

Ein persönlicher, empathischer Ernährungs-Coach basierend auf Google Gemini (`gemini-2.5-flash`) und Streamlit.

## Lokales Ausführen

1. Virtuelle Umgebung anlegen & Abhängigkeiten installieren:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. API-Key hinterlegen:
   Erstelle `.streamlit/secrets.toml` mit folgendem Inhalt:
   ```toml
   GEMINI_API_KEY = "dein_gemini_api_key"
   ```
   (Oder setze die Umgebungsvariable `export GEMINI_API_KEY="dein_key"`).

3. Streamlit App starten:
   ```bash
   streamlit run app.py
   ```

## Deployment auf Streamlit Community Cloud

1. Repository auf GitHub pushen.
2. Auf [share.streamlit.io](https://share.streamlit.io/) mit GitHub anmelden.
3. Neues App-Deployment auswählen (`app.py` als Main file).
4. In den **Advanced Settings** unter **Secrets** eintragen:
   ```toml
   GEMINI_API_KEY = "dein_gemini_api_key"
   ```
5. Auf **Deploy** klicken!

