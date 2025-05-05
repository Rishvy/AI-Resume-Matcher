# 🤖 AI Resume Matcher (not completed)

AI Resume Matcher is an intelligent system designed to compare resumes with job descriptions using NLP and vector embeddings, providing match scores to help identify the most suitable candidates for a role.

---

## 📁 Project Structure

```
AI-Resume-Matcher/
├── embedding_model.py       # Generates embeddings from text
├── job_crawler.py           # Scrapes job descriptions from job portals
├── main.py                  # Main application entry point
├── matcher.py               # Computes similarity between resumes and job listings
├── resume_parser.py         # Extracts and parses resume content
├── vector_db.py             # Stores and manages vectorized data
├── requirements.txt         # List of Python dependencies
├── Procfile                 # Deployment configuration
└── README.md                # Project documentation
```

---

## 🚀 Features

- 📄 Resume PDF parsing and extraction
- 🌐 Real-time job description scraping (in development)
- 🧠 Text embeddings using language models (e.g., Groq API, Sentence Transformers)
- 🔍 Cosine similarity for job-resume matching
- 🗃️ Vector database integration for fast search and retrieval

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rishvy/AI-Resume-Matcher.git
   cd AI-Resume-Matcher
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Usage

1. Place your resume files (PDF) in the designated directory.
2. Run the main script:
   ```bash
   python main.py
   ```
3. The script will:
   - Parse resumes
   - Fetch or load job descriptions
   - Generate embeddings
   - Match jobs with resumes
   - Print top matches with similarity scores

---

## ✅ Example (Coming Soon)

Sample output:

```
Resume: john_doe_resume.pdf
Top Matching Jobs:
1. Data Scientist – 93.2%
2. Machine Learning Engineer – 89.5%
3. AI Research Assistant – 88.1%
```

---
