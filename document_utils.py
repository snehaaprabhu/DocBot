import fitz
import pandas as pd

def extract_text(file):
    if file.type == "application/pdf":
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join(page.get_text() for page in doc)
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    elif file.type == "text/csv":
        df = pd.read_csv(file)
        return df.to_string(index=False)
    else:
        return ""

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def load_and_chunk_docs(files):
    all_chunks = []
    for file in files:
        text = extract_text(file)
        chunks = chunk_text(text)
        all_chunks.extend(chunks)
    return all_chunks
