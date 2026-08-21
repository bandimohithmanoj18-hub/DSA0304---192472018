import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text = "The quick brown fox jumps over the lazy dog."

words = nltk.word_tokenize(text)

tags = nltk.pos_tag(words)

print("Part of Speech Tags:\n")

for word, tag in tags:
    print(word, ":", tag)
