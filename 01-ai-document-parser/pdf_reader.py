
from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str | Path) -> str:
    """Extract selectable text from a PDF invoice."""
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("The input file must be a PDF.")

    reader = PdfReader(str(path))

    if reader.is_encrypted:
        raise ValueError("Encrypted PDFs are not supported.")

    pages = []

    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)

    extracted_text = "\n".join(pages).strip()

    if not extracted_text:
        raise ValueError(
            "No selectable text found. This PDF may be scanned "
            "and require OCR."
        )

    return extracted_text


if __name__ == "__main__":
    pdf_file = input("Enter the PDF file path: ").strip().strip('"')

    try:
        text = extract_text_from_pdf(pdf_file)
        print("\n--- Extracted PDF Text ---\n")
        print(text)

    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
