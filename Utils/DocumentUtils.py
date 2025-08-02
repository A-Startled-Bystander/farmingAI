import os
import time

import fitz # PyMuPDF
from dotenv import load_dotenv
from pymupdf import Document

def retrieve_doc_name(path: str):
    return path.split("\\")[-1]

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

    # search = page.search_for("Contents")
    # if len(search) > 0:
    #     print()

    return {
        "FILE_NAME": filename,
        "PAGES": pages
    }


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

# def identify_table_of_contents(pages):
#     for page in pages:
#         if "Contents" in page["page_content"]:
#
#             break
#
#     # If we cant find a page specifying "Contents" we will need to check with the LLM if any pages ID as a TOC
#     return None
