from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file.
    """

    reader = PdfReader(pdf_path)

    extracted_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            extracted_text += text + "\n"
    print(f"Extracted Text Length: {len(extracted_text)} characters")
    print(f"Extracted Text Preview: {extracted_text[:500]}...")  # Print the first 500 characters as a preview
    return extracted_text