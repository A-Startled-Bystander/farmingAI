import time

import fitz # PyMuPDF
from pymupdf import Document


def convert_pdf_to_text(path: str):
    print("begin extraction of pdf text")
    start = time.time()
    pages = []

    doc : Document = fitz.open(path)
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            pages.append({
                "page_num": i,
                "page_content": text
            })
    doc.close()

    print("Text extraction completed in", round(time.time() - start, 2), "seconds")
    print("Text extraction completed")
    return pages

def identify_table_of_contents(pages):
    for page in pages:
        if "Contents" in page["page_content"]:

            break

    # If we cant find a page specifying "Contents" we will need to check with the LLM if any pages ID as a TOC
    return None
