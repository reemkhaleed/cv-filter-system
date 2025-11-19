import os
import shutil
import zipfile
from docx import Document
import PyPDF2


KEYWORDS = ["python", "machine learning", "excel", "data analysis"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_FILE = os.path.join(BASE_DIR, "linkedin_applicants.zip")

INPUT_FOLDER = os.path.join(BASE_DIR, "cvs")
MATCH_FOLDER = os.path.join(BASE_DIR, "match")
NO_MATCH_FOLDER = os.path.join(BASE_DIR, "do_not_match")

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(MATCH_FOLDER, exist_ok=True)
os.makedirs(NO_MATCH_FOLDER, exist_ok=True)



if os.path.exists(ZIP_FILE):
    print(" Found LinkedIn ZIP file. Extracting...")
    with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall(INPUT_FOLDER)
    print("✅ All CVs extracted to /cvs folder.\n")
else:
    print("No ZIP file found. Place your LinkedIn ZIP as: linkedin_applicants.zip\n")


def read_pdf(file_path):
    text = ""
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    except:
        pass
    return text.lower()


def read_docx(file_path):
    text = ""
    try:
        doc = Document(file_path)
        for p in doc.paragraphs:
            text += p.text + "\n"
    except:
        pass
    return text.lower()


def read_txt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().lower()
    except:
        return ""


def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)
    elif file_path.endswith(".docx"):
        return read_docx(file_path)
    elif file_path.endswith(".txt"):
        return read_txt(file_path)
    else:
        return ""


def contains_keywords(text):
    return any(keyword.lower() in text for keyword in KEYWORDS)



print("🔍 Filtering CVs...")

for filename in os.listdir(INPUT_FOLDER):
    file_path = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(file_path):
        continue

    text = extract_text(file_path)

    if contains_keywords(text):
        shutil.copy(file_path, MATCH_FOLDER)
        print(f"[MATCH] {filename}")
    else:
        shutil.copy(file_path, NO_MATCH_FOLDER)
        print(f"[NO MATCH] {filename}")

print("\n Filtering completed!")
print(f"Matched → {MATCH_FOLDER}")
print(f"Not matched → {NO_MATCH_FOLDER}")
