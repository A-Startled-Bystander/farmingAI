import spacy

# NB
# Load spaCy model (download once: python -m spacy download en_core_web_sm)

def check_spacy_model():
    try:
        nlp = spacy.load("en_core_web_sm")
        # Test on a simple sentence
        doc = nlp("Hello world")
        if len(doc) > 0:
            print("spaCy model loaded successfully!")
        return nlp
    except OSError:
        print("Failed to load spaCy model 'en_core_web_sm'. Make sure it is installed.")
        print("You can install it with: python -m spacy download en_core_web_sm")
        return None

test = check_spacy_model()