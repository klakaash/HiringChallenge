import spacy
nlp = spacy.load("en_core_web_sm")

def get_medicine_name(sentence):
    """ extract the medicine name from the sentence """
    doc = nlp(sentence)
    if not doc.ents:
        return ""
    matched_entity = doc.ents[0]

    return matched_entity.text