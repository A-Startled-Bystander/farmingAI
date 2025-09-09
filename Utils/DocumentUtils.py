import os
import re
import time

import fitz # PyMuPDF
from dotenv import load_dotenv
from pymupdf import Document



def retrieve_doc_name(path: str):
    return path.split("\\")[-1]

# Ensure the file can be opened, read and saved, otherwise discard it as corrupted
def verify_file_validity(path: str):
    filename = retrieve_doc_name(path)
    try:
        doc: Document = fitz.open(path)
        if doc.page_count == 0:
            return {
                "FILE_NAME": filename,
                "VALIDITY": False,
                "REASON": "No Pages Found"
            }
        for page_number in range(len(doc)):
            try:
                page = doc.load_page(page_number)
            except Exception as e:
                return {
                    "FILE_NAME": filename,
                    "VALIDITY": False,
                    "REASON": f"Could Not Load Page {page_number}"
                }

    except Exception as e:
        return {
            "FILE_NAME": filename,
            "VALIDITY": False,
            "REASON": "Could Not Open"
        }

    try:
        load_dotenv()
        save_path = os.getenv("VALIDATED_DOC_FILE_LOCATION") + filename
        temp_path = save_path + ".tmp"

        doc.save(temp_path)
        os.replace(temp_path, save_path)

    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)

        return {
            "FILE_NAME": filename,
            "VALIDITY": False,
            "REASON": "Could Not Save"
        }


    return {
        "FILE_NAME": filename,
        "VALIDITY": True,
        "REASON": "All pages Loaded"
    }

def retrieve_pages(path: str):
    filename = retrieve_doc_name(path)
    pages = []
    doc: Document = fitz.open(path)
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        pages.append(page)

    return {
        "FILE_NAME": filename,
        "PAGES": pages
    }


