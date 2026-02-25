from io import BytesIO

from docx import Document
from pypdf import PdfReader


class TextExtractionError(Exception):
    pass


def clean_text(raw_text: str) -> str:
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
    return " ".join(lines)


def extract_text_from_pdf(content: bytes) -> str:
    reader = PdfReader(BytesIO(content))
    text = " ".join((page.extract_text() or "") for page in reader.pages)
    if not text.strip():
        raise TextExtractionError("No readable content found in PDF")
    return clean_text(text)


def extract_text_from_docx(content: bytes) -> str:
    document = Document(BytesIO(content))
    text = " ".join(paragraph.text for paragraph in document.paragraphs)
    if not text.strip():
        raise TextExtractionError("No readable content found in DOCX")
    return clean_text(text)


def extract_resume_text(content: bytes, filename: str) -> str:
    filename_lower = filename.lower()
    if filename_lower.endswith(".pdf"):
        return extract_text_from_pdf(content)
    if filename_lower.endswith(".docx"):
        return extract_text_from_docx(content)
    raise TextExtractionError("Unsupported file type. Use PDF or DOCX")
