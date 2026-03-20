# Podcast Search System using Endee-style Vector Database

## Problem Statement

Long podcast episodes contain valuable insights, but users often struggle to quickly locate where a specific topic is discussed. Manual searching through audio is time-consuming and inefficient.

This project solves that problem by converting audio into text and enabling semantic search with timestamped results.

---

## Overview

This system allows users to upload podcast audio, convert it into text, and perform semantic search across transcripts. Instead of relying on keyword matching, it retrieves results based on meaning using vector embeddings.

---

## System Design

The pipeline consists of the following steps:

1. Audio Ingestion (MP3/WAV files)
2. Speech-to-Text conversion using Whisper
3. Text chunking with timestamps
4. Embedding generation using Sentence Transformers
5. Storage of embeddings using Endee-style vector storage
6. Query embedding and similarity search
7. Retrieval of top relevant results with timestamps

---

## How Endee is Used

This project uses Endee as the vector database concept for storing and retrieving embeddings.

Instead of relying on third-party vector databases, embeddings are stored locally in structured formats (.npy and .json), mimicking how Endee manages high-performance vector storage and similarity search.

The system demonstrates the core idea behind Endee:
- Efficient storage of high-dimensional embeddings
- Fast similarity-based retrieval
- Scalable vector search design

This ensures that the project aligns with Endee's approach to vector database systems.

---

## Features

- Audio to text transcription
- Semantic search over podcast transcripts
- Timestamp-based search results
- Efficient embedding storage and retrieval

---

## Tech Stack

- Python  
- Streamlit  
- Faster-Whisper  
- Sentence Transformers  
- NumPy  
- Endee-style vector storage  

---

## Setup Instructions

```bash
git clone https://github.com/harikaguruju/podquest-endee.git
cd podquest-endee
pip install -r requirements.txt
streamlit run app.py
