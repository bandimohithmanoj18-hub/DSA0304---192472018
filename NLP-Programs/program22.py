text = "Ravi went to the shop. He bought a book."

words = text.split()

for i, word in enumerate(words):
    if word.lower() == "he":
        words[i] = "Ravi"

print(" ".join(words))
