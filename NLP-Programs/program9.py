import re

sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nRule-Based POS Tags:\n")

for word in words:

    if re.fullmatch(r".*ing", word):
        tag = "VBG"

    elif re.fullmatch(r".*ed", word):
        tag = "VBD"

    elif re.fullmatch(r".*ly", word):
        tag = "RB"

    elif re.fullmatch(r".*ness", word):
        tag = "NN"

    elif re.fullmatch(r".*ment", word):
        tag = "NN"

    elif re.fullmatch(r".*s", word):
        tag = "NNS"

    elif word[0].isupper():
        tag = "NNP"

    else:
        tag = "NN"

    print(word, ":", tag)
