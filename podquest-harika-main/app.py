import os, json
import streamlit as st
from pathlib import Path

from podquest.transcribe import transcribe_file, read_transcript
from podquest.config import DEFAULT_WHISPER_MODEL, DEFAULT_COMPUTE_TYPE
from podquest.indexer import build_index
from podquest.retrieve import search

TRANSCRIPTS_DIR = Path("transcripts")
TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

st.title("🎙 Podcast Search System")

# -------------------------------
# 🔹 Upload Section
# -------------------------------
st.header("Ingest & Transcribe")

uploaded_files = st.file_uploader(
    "Upload episodes", type=["mp3", "wav"], accept_multiple_files=True
)

saved_paths = []
if uploaded_files:
    for uf in uploaded_files:
        save_path = Path("data") / uf.name
        save_path.parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(uf.getbuffer())
        st.success(f"Saved: {save_path}")
        saved_paths.append(str(save_path))

# -------------------------------
# 🔹 Transcription
# -------------------------------
if st.button("Transcribe all") and saved_paths:
    for p in saved_paths:
        with st.spinner(f"Transcribing {os.path.basename(p)} ..."):
            result = transcribe_file(
                audio_path=p,
                out_dir=str(TRANSCRIPTS_DIR),
                model_size=DEFAULT_WHISPER_MODEL,
                compute_type=DEFAULT_COMPUTE_TYPE,
            )
        st.success(f"Saved transcript: {result['json_path']}")

        st.subheader(f"Transcript: {os.path.basename(result['json_path'])}")
        st.text_area("Full transcript", value=result["text"], height=220)

# -------------------------------
# 🔹 View Existing Transcripts
# -------------------------------
st.markdown("---")
st.header("View Transcripts")

existing = sorted([p for p in TRANSCRIPTS_DIR.glob("*.json")])

if existing:
    pick = st.selectbox(
        "Select transcript",
        options=[str(p) for p in existing],
        format_func=lambda p: os.path.basename(p),
    )

    if pick:
        data = read_transcript(pick)
        st.text_area("Transcript", value=data["text"], height=200)

else:
    st.info("No transcripts available")

# -------------------------------
# 🔹 Indexing (Endee-style)
# -------------------------------
st.markdown("---")
st.header("📦 Create Vector Index")

if st.button("Create Index"):
    with st.spinner("Indexing transcripts..."):
        count, _ = build_index(str(TRANSCRIPTS_DIR))
    st.success(f"Indexed {count} chunks successfully")

# -------------------------------
# 🔹 Search Section
# -------------------------------
st.markdown("---")
st.header("🔍 Search Podcasts")

query = st.text_input("Enter your question")

if query:
    results = search(query)

    if results:
        for r in results:
            st.subheader(f"📌 Episode: {r['episode']}")
            st.write(f"⏱ {r['start']} - {r['end']}")
            st.write(f"⭐ Score: {r['score']:.4f}")
            st.markdown("---")
    else:
        st.warning("No results found")
