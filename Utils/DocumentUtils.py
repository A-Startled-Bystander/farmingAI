import re
import pymupdf

from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO

def convert_pdf_to_text(path: str):
    print("begin extraction of pdf text")
    output = StringIO()
    with open(path, "rb") as f:
        extract_text_to_fp(
            f,
            output,
            laparams=LAParams(),
            output_type='text',
            codec=None
        )

    text = output.getvalue()
    output.close()
    del output
    print("Text extraction completed")
    return text

def split_page_breaks(pdf_text: str):
    pages = pdf_text.split("\x0c") #Split at every page break
    return_pages = []
    for i, page in enumerate(pages, 1):
        if page.strip() != '' and page.strip() != '\n':
            return_pages.append({
                "page_num": i,
                "page_content": page
            })
    return return_pages
