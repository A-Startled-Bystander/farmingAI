import os

from Utils.DocumentUtils import convert_pdf_to_text

currentDirectory = os.path.dirname(os.path.abspath(__file__))
exampleDoc = "Soilless Culture - Use of Substrates for the Production of Quality Horticultural Crops (Md. Asaduzzaman) (Z-Library).pdf"
# exampleDoc = "Agricultural_Innovation_and_Sustainable_Development.pdf"
PDF_PATH = currentDirectory + "\\Data\\Documents\\" + exampleDoc


# text = extract_text_from_doc(PDF_PATH)
pages = convert_pdf_to_text(PDF_PATH)
print()

