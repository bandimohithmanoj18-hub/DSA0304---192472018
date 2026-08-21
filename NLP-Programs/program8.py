import random

# Training data
training = [
    ("The", "DT"),
    ("dog", "NN"),
    ("barks", "VBZ"),
    ("A", "DT"),
    ("cat", "NN"),
    ("runs", "VBZ"),
    ("Bird", "NN"),
    ("flies", "VBZ")
]

# Build probability model
model = {}

for word, tag in training:
    word = word.lower()

    if word not in model:
        model[word] = []

    model[word].append(tag)

sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nTagged Sentence:\n")

for word in words:
    tags = model.get(word.lower(), ["NN"])
    print(word, ":", random.choice(tags))_
