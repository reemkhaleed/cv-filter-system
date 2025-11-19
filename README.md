# CV Filter System (Keyword-Based)

This Python script automatically filters CV files based on keywords. It extracts text from PDFs, DOCX documents, and TXT files, checks for target keywords, and then sorts the CVs into two folders:

- `match/` → CV contains at least one keyword  
- `do_not_match/` → CV does not contain any keywords  

It also supports importing a LinkedIn applicant ZIP file automatically.

---

## 🔍 Features
- Reads **PDF**, **DOCX**, and **TXT** CVs.
- Automatically extracts text.
- Keyword-based filtering (Python, Excel, Machine Learning, etc.).
- Creates output folders automatically.
- Supports LinkedIn applicant export ZIP files.
- Clean and fast filtering — works with large batches of CVs.

## Install dependencies:
  ```bash
pip install -r requirements.txt
 ```
---

## How To Use :
1.Place your LinkedIn exported ZIP file as:
```bash
linkedin_applicants.zip
 ```

2.Run the script:
```bash
python Cv_filter.py
 ```

3.Results:

- Matched CVs → match/

- Not matched → do_not_match/

- Extracted files → cvs/
