def parser(word):

    irregular = {
        "children": "child",
        "men": "man",
        "women": "woman",
        "mice": "mouse",
        "feet": "foot"
    }

    if word in irregular:
        return irregular[word], "Plural Noun"

    if word.endswith("ies"):
        return word[:-3] + "y", "Plural Noun"

    if word.endswith("es"):
        return word[:-2], "Plural Noun"

    if word.endswith("s"):
        return word[:-1], "Plural Noun"

    return word, "Singular"


words = ["cars", "boxes", "cities", "children"]

for w in words:
    print(w, "->", parser(w))
