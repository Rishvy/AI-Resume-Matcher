import os
import pdfplumber
import docx2txt

def extract_resume_text(file_path):
    file_path = file_path.strip()

    # Extract file extension
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text: 
                        text += page_text
                    else:
                        raise ValueError(f"Empty text found on page {pdf.pages.index(page)+1}")
        except Exception as e:
            raise ValueError(f"Error extracting text from PDF: {str(e)}")
        return text

    elif ext == ".docx":
        try:
            return docx2txt.process(file_path)
        except Exception as e:
            raise ValueError(f"Error extracting text from DOCX: {str(e)}")
    
    else:
        raise ValueError(f"Unsupported file format '{ext}'. Only PDF or DOCX are allowed.")