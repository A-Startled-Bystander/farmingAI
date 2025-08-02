from datetime import datetime
import json
import os

from dotenv import load_dotenv

from Utils.DocumentUtils import convert_pdf_to_text, retrieve_pages, verify_file_validity

currentDirectory = os.path.dirname(os.path.abspath(__file__))
exampleDoc = "Soilless Culture - Use of Substrates for the Production of Quality Horticultural Crops (Md. Asaduzzaman) (Z-Library).pdf"
# exampleDoc = "Agricultural_Innovation_and_Sustainable_Development.pdf"
PDF_PATH = currentDirectory + "\\Data\\Documents\\" + exampleDoc



# pages = convert_pdf_to_text(PDF_PATH)
# file_validity = verify_file_validity(PDF_PATH)
#



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


validate_file_sources()
print("File Scan Complete")
