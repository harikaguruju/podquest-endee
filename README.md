# PodQuest – Podcast Semantic Search System

## 📌 Problem Statement
Long podcast episodes contain valuable insights, but users cannot quickly find where a specific topic is discussed. Manual searching is slow and inefficient.

This project solves the problem by making podcast audio semantically searchable with timestamped results.

---

## 🚀 Project Overview
PodQuest is an AI-powered system that:
- Converts podcast audio into text
- Indexes the content using vector embeddings
- Enables semantic search across episodes
- Returns exact timestamps for relevant results

---

## ⚙️ Features
- 🎧 Upload podcast audio (MP3, WAV)
- 📝 Automatic transcription using Faster-Whisper
- 🔍 Semantic search using vector embeddings
- ⏱ Timestamp-based retrieval
- 📊 Interactive UI using Streamlit

---

## 🧠 Tech Stack
- Python
- Streamlit
- Faster-Whisper
- Sentence Transformers
- **Endee (Vector Database)**
- NumPy / Pandas

---

## 🔄 System Architecture
1. **Ingestion** – Upload audio files  
2. **Transcription** – Convert audio → text using Whisper  
3. **Chunking** – Split transcript into smaller segments  
4. **Embedding** – Convert text chunks into vectors  
5. **Indexing (Endee)** – Store embeddings in Endee vector database  
6. **Retrieval** – Search relevant chunks using semantic similarity  
7. **Response** – Return transcript + timestamps  

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
