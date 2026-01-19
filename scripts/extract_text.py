import os
from docx import Document
import pdfplumber

RAW_DOCS_DIR = "data/raw_docs"
RAW_TEXT_DIR = "data/raw_text"

os.makedirs(RAW_TEXT_DIR, exist_ok=True)

def extract_from_docx(file_path):
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text.strip())
    return "\n".join(text)

def extract_from_pdf(file_path):
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

for filename in os.listdir(RAW_DOCS_DIR):
    file_path = os.path.join(RAW_DOCS_DIR, filename)

    if filename.lower().endswith(".docx"):
        text = extract_from_docx(file_path)

    elif filename.lower().endswith(".pdf"):
        text = extract_from_pdf(file_path)

    else:
        continue

    output_name = os.path.splitext(filename)[0] + ".txt"
    output_path = os.path.join(RAW_TEXT_DIR, output_name)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Extracted: {filename} → {output_name}")
