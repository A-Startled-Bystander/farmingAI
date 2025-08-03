import re
from datetime import datetime
import json
import os

from dotenv import load_dotenv
from pymupdf import Page

from Utils.DocumentUtils import retrieve_pages, verify_file_validity

currentDirectory = os.path.dirname(os.path.abspath(__file__))
exampleDoc = "Soilless Culture - Use of Substrates for the Production of Quality Horticultural Crops (Md. Asaduzzaman) (Z-Library).pdf"
# exampleDoc = "Agricultural_Innovation_and_Sustainable_Development.pdf"
PDF_PATH = currentDirectory + "\\Data\\Documents\\" + exampleDoc


def validate_file_sources():
    load_dotenv()
    unvalidated_files_path = os.getenv("UNVALIDATED_DOC_FILE_LOCATION")
    sub_dir = os.listdir(unvalidated_files_path)
    print()

    log_name = f"farm_docs_failed_validity_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt"
    open(log_name, "x")
    with open(log_name, "w") as log:

        for folder in sub_dir:
            log.write("\n")
            sub_dir_path = unvalidated_files_path + folder + "\\"

            files = os.listdir(sub_dir_path)
            log.write(f"Parent DIRECTORY: {sub_dir_path}" + "\n")
            log.write("--------------------------------------------------" + "\n")
            for file in files:
                file_path = sub_dir_path + file
                file_validity = verify_file_validity(file_path)
                if not file_validity["VALIDITY"]:
                    json_line = json.dumps(file_validity)
                    log.write(json_line + "\n")


def retrieve_content_headers(filePath: str):
    doc_pages = retrieve_pages(filePath)
    toc_object, toc_found = search_toc(doc_pages)

# Search for table of contents in specified doc
def search_toc(doc_pages):
    toc_found = False
    text_list = []
    for page in doc_pages["PAGES"][:10]: #Only grab first 10 pages
        search_page = page.search_for("Contents") #search_for is not case sensitive, will pick up any mention of desired word
        if len(search_page) > 0:
            x0, y0, x1, y1 = search_page[0] #Get box boundry of match

            # Filter based on coordinates (e.g., y0 near top of page)
            if y0 < 100:  # Likely near the top
                toc_found = True
                text_info = page.get_text("dict") #Grabs all metadata
                # page_text = page.get_text().strip()
                for block in text_info["blocks"]:
                    if "lines" in block:
                        block_text = ""
                        for line in block["lines"]:
                            for span in line["spans"]:
                                block_text = block_text + span["text"]

                        clean_block_text = re.sub(r'\s+', ' ', block_text).strip()
                        if clean_block_text:
                            text_list.append(clean_block_text)

    filtered_list = [text for text in text_list if "Contents" not in text]
    print()

    return None, toc_found

retrieve_content_headers(PDF_PATH)
print()