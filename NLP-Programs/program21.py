import spacy

nlp = spacy.load("en_core_web_sm")

text = "The student reads a book."
doc = nlp(text)

for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)
    print("Meaning:", "person/object/entity")
