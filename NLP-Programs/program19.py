from nltk.corpus import wordnet as wn
import nltk

nltk.download("wordnet")

def lesk(word, sentence):
    best = None
    max_overlap = 0

    for syn in wn.synsets(word):
        definition = set(syn.definition().lower().split())
        overlap = len(definition.intersection(sentence.lower().split()))

        if overlap > max_overlap:
            max_overlap = overlap
            best = syn

    return best

result = lesk("bank", "I deposited money in the bank")

print(result)
