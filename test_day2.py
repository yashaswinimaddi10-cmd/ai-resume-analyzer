from resume_parser import extract_text
from text_cleaner import clean_text

path = "sample_resumes/fake_resume_aarav.pdf"

with open(path, "rb") as f:
    raw = extract_text(f, path)

print("--- RAW (first 400 characters) ---")
print(raw[:400])

print("\n--- CLEANED (first 400 characters) ---")
print(clean_text(raw)[:400])

print("\n--- SYMBOL TEST ---")
print(clean_text("I know C++, C#, .NET and Python."))