from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "organization",
    "organizer",
    "organizing",
    "organized",
    "organization's"
]

for word in words:
    print(word, "->", ps.stem(word))
