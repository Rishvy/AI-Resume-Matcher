import streamlit as st
import tempfile
import json
import requests
import os
import numpy as np
from dotenv import load_dotenv
from resume_parser import extract_resume_text
from embedding_model import get_embedding
from vector_db import save_resume_embedding, load_faiss_index
from matcher import match_jobs

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
groq_api_base = "https://api.groq.com/openai/v1"

def parse_resume_with_groq(resume_text):
    url = f"{groq_api_base}/chat/completions"
    prompt = """
    You are a resume parser. Extract the following from this resume:
    - Name
    - Years of Experience
    - Skills (as a list)
    - Technologies (as a list)
    - Location
    - Education

    Resume:
    """
    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are an expert resume parser."},
            {"role": "user", "content": prompt + resume_text}
        ],
        "temperature": 0.2
    }

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

st.title("📄 AI Job Finder")

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    file_ext = os.path.splitext(uploaded_file.name)[1].lower()
    if file_ext not in [".pdf", ".docx"]:
        st.error("Unsupported file format. Only PDF or DOCX allowed.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        try:
            resume_text = extract_resume_text(tmp_path)
            st.subheader("📜 Extracted Resume Text")
            st.text(resume_text[:1000])  # Show partial text

            if st.button("Parse Resume"):
                parsed_data = parse_resume_with_groq(resume_text)
                st.subheader("🧠 Parsed Data")
                st.json(parsed_data)

                embedding = get_embedding(resume_text)
                st.success("✅ Embedding generated")
                st.write("Vector size:", len(embedding))

                save_resume_embedding(embedding)

                st.subheader("🔍 Matching Jobs")
                matches = match_jobs(embedding)
                for match in matches:
                    job = match["job"]
                    st.write(f"**{job['title']}** at **{job['company']}**")
                    st.write(f"Location: {job['location']}")
                    st.write(f"Similarity Score: {match['similarity']:.2f}")
                    st.write(f"[Apply Here]({job['url']})")
                    st.markdown("---")

        except ValueError as e:
            st.error(f"Error: {str(e)}")