# Initial dictionary
dictionary = {
    "I": "PRP",
    "can": "NN",
    "fish": "NN",
    "run": "VB",
    "dogs": "NNS",
    "quickly": "RB"
}

sentence = input("Enter a sentence: ")

words = sentence.split()

tags = []

# Initial tagging
for word in words:
    tags.append(dictionary.get(word, "NN"))

# Transformation Rules
for i in range(len(words)):

    # Rule 1
    if words[i] == "can" and i > 0 and tags[i-1] == "PRP":
        tags[i] = "MD"

    # Rule 2
    if words[i].endswith("ing"):
        tags[i] = "VBG"

    # Rule 3
    if words[i].endswith("ed"):
        tags[i] = "VBD"

print("\nTransformation-Based POS Tags:\n")

for word, tag in zip(words, tags):
    print(word, ":",) 
