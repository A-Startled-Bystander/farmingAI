import re

import spacy

from Identifiers.ChapterIdentifier import is_likely_person_name


# NB
# Load spaCy model (download once: python -m spacy download en_core_web_sm)

def check_spacy_model():
    try:
        nlp = spacy.load("en_core_web_sm")
        # Test on a simple sentence
        doc = nlp("Hello World")
        if len(doc) > 0:
            print("spaCy model loaded successfully!")
        return nlp
    except OSError:
        print("Failed to load spaCy model 'en_core_web_sm'. Make sure it is installed.")
        print("You can install it with: python -m spacy download en_core_web_sm")
        return None

nlp = check_spacy_model()
# print(is_likely_person_name('by J.A. Olfati', nlp))
#
# print(bool(re.match(r'^([A-Z]\.)+ [A-Z][a-z]+$', "by J.A. Olfati")))