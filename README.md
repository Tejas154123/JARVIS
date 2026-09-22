# 🧠 Jarvis - Voice-Controlled AI Assistant (Offline + Smart)

Welcome to the **Jarvis** project — a fully customizable, offline-friendly voice assistant that listens, responds, and performs various tasks on your PC with real-time interaction.

---

## 🚀 Features

### 🎙️ Voice Activation & Interaction
- **Wake Word Detection**: Say “Jarvis” once to activate
- **Sleep Mode**: Say “sleep” to deactivate listening
- **Continuous Response**: Jarvis replies to each command using voice (`pyttsx3`)

### 🧠 Built-in Knowledge Base
- ✅ 30 General Knowledge (GK) questions
- ✅ 30 Physics questions
- Smart fallback if it can't find answers

### 📰 News Integration
- Get real-time **top headlines** using [NewsAPI](https://newsapi.org)
- Jarvis reads headlines aloud

### 🕰️ Real-Time Utilities
- Current time/date queries
- Wikipedia summaries
- Tech jokes via `pyjokes`

### 🌐 Web & App Integration
- Open apps like **Spotify**, **Notepad**, **Calculator**, etc.
- Open websites like **YouTube**, **Google**, **Wikipedia**, etc.

### 🔊 Offline Ready
- Fully functional without internet (except web, Wikipedia, news)

---

## 🧩 Requirements
Use this URL if you are using openrouter api key:
https://openrouter.ai/api/v1/chat/completions

Suggested AI model: "openai/gpt-4o-mini"


Install all the required libraries using:
```bash
pip install pyttsx3
pip install speechrecognition
pip install pyaudio
pip install wikipedia
pip install requests
pip install pywhatkit
pip install pyjokes
