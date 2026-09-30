from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:          # go through every page
        page_text = page.extract_text()
        if page_text:                  # some pages may be empty
            text += page_text + "\n"
    return text


def extract_text_from_docx(file):
    doc = Document(file)
    # a Word file is a list of paragraphs, so join them all
    return "\n".join(p.text for p in doc.paragraphs)


def extract_text(file, filename):
    name = filename.lower()
    if name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif name.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        raise ValueError("Only PDF and DOCX files are supported.")