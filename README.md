# PodQuest – Podcast Search System

## 📌 Problem Statement
Long podcast episodes contain valuable insights, but it is difficult to quickly find where a specific topic is discussed. Manual searching is slow and inefficient.

This project solves that problem by converting podcast audio into searchable text with timestamps.

---

## 🚀 Project Overview
PodQuest is an AI-powered system that allows users to:
- Upload podcast audio files
- Convert audio into text using speech recognition
- Search for topics within podcasts
- Get exact timestamps where topics are discussed

---

## ⚙️ Features
- 🎧 Audio upload (MP3, WAV)
- 📝 Automatic transcription using Faster-Whisper
- 🔍 Semantic search using embeddings
- ⏱ Timestamp-based results
- 📊 Clean UI using Streamlit

---

## 🧠 Tech Stack
- Python
- Streamlit
- Faster-Whisper
- Sentence Transformers
- ChromaDB
- NumPy / Pandas

---

## 🔄 How It Works
1. Upload podcast audio
2. Audio is transcribed into text
3. Text is split into chunks
4. Chunks are converted into embeddings
5. Stored in vector database (ChromaDB)
6. User searches → relevant chunks retrieved with timestamps

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
