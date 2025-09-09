import re
import spacy



def is_likely_person_name(text: str, nlp: spacy.Language):
    text = text.strip()
    if not text or len(text) < 2:
        return False

    initials = is_likely_initial_name(text)
    if initials:
        return True

    doc = nlp(text)
    return any(ent.label_ == "PERSON" for ent in doc.ents)

def is_likely_initial_name(text: str):
    # Remove "by" at the start
    text = re.sub(r'^\s*by\s+', '', text, flags=re.IGNORECASE)

    # Matches "J.A. Olfati", "M. Smith", "A.B.C. Johnson"
    return bool(re.match(r'^([A-Z]\.)+ [A-Z][a-z]+$', text))