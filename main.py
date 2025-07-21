import os

from Utils.DocumentUtils import convert_pdf_to_text, split_page_breaks
from Utils.LLMUtils import identify_table_of_contents

currentDirectory = os.path.dirname(os.path.abspath(__file__))
exampleDoc = "Soilless Culture - Use of Substrates for the Production of Quality Horticultural Crops (Md. Asaduzzaman) (Z-Library).pdf"
PDF_PATH = currentDirectory + "\\Data\\Documents\\" + exampleDoc


# text = extract_text_from_doc(PDF_PATH)
text = convert_pdf_to_text(PDF_PATH)
pages = split_page_breaks(text)
identify_table_of_contents(pages[:10])
print()

