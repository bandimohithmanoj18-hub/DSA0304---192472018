tags = {
    "the":"DT",
    "student":"NN",
    "is":"VBZ",
    "reading":"VBG",
    "a":"DT",
    "book":"NN",
    "he":"PRP",
    "likes":"VBZ",
    "python":"NN"
}

s = input("Enter sentence: ").lower().split()

for word in s:
    if word in tags:
        tag = tags[word]
    elif word.endswith("ing"):
        tag = "VBG"
    elif word.endswith("ly"):
        tag = "RB"
    else:
        tag = "NN"

    print(word, "/", tag)
