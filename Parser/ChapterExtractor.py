# Search for table of contents in specified doc
import re

from Identifiers.ChapterIdentifier import is_likely_person_name
from Transformer.ChapterTransformer import break_keywords, refine_header_string
from Utils.SpaceyUtils import check_spacy_model


def search_toc(doc_pages):
    toc_found = False
    text_list = []
    for page in doc_pages["PAGES"][:10]: #Only grab first 10 pages
        search_page = page.search_for("Contents") #search_for is not case sensitive, will pick up any mention of desired word
        # print()
        if len(search_page) > 0:
            x0, y0, x1, y1 = search_page[0] #Get box boundry of match

            # Filter based on coordinates (e.g., y0 near top of page)
            if y0 < 100:  # Likely near the top
                toc_found = True
                text_info = page.get_text("dict") #Grabs all metadata
                # page_text = page.get_text().strip()
                for block in text_info["blocks"]:
                    if "lines" in block:
                        block_text_list = []
                        for line in block["lines"]:
                            for span in line["spans"]:
                                clean_block_text = re.sub(r'\s+', ' ', span["text"]).strip()

                                if clean_block_text:
                                    block_text_list.append(clean_block_text)

                        # clean_block_text = re.sub(r'\s+', ' ', block_text).strip()
                        if len(block_text_list) > 0:
                            text_list.append(block_text_list)

    filtered_list = [text for text in text_list if "Contents" not in text]
    return filtered_list, toc_found

# Refine the headers found to exclude authors and other undesired words
def refine_toc_object(toc_object):
    nlp = check_spacy_model()
    refined_toc_list = []
    print()
    toc_object = break_keywords(toc_object)
    print()
    if nlp:
        for header_object in toc_object:
            header_list = []
            for content_line in header_object:
                person_name = is_likely_person_name(content_line, nlp)
                print()
                if not person_name:
                    # refined_content_line = refined_content_line + " " + content_line
                    header_list.append(content_line)
            if len(header_list) > 0:
                refined_content_line = " ".join(header_list)
                refined_toc_list.append(refine_header_string(refined_content_line))
    else:
        return None
    return refined_toc_list