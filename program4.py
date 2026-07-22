def plural(word):
    word = word.strip()

    if not word:
        return "Invalid Input"

    if word.endswith(("s", "ss", "sh", "ch", "x", "z")):
        return word + "es"

    elif word.endswith("y") and len(word) > 1 and word[-2].lower() not in "aeiou":
        return word[:-1] + "ies"

    elif word.endswith("fe"):
        return word[:-2] + "ves"

    elif word.endswith("f") and not word.endswith("ff"):
        return word[:-1] + "ves"

    elif word.endswith("o") and len(word) > 1 and word[-2].lower() not in "aeiou":
        return word + "es"

    else:
        return word + "s"


n = int(input("Enter number of words: "))

for _ in range(n):
    word = input("Enter word: ")
    print("Plural:", plural(word))