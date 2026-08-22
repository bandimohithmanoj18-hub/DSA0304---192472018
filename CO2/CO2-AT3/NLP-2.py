words = [
    "happiest",
    "unbelievable",
    "running",
    "reordering",
    "smartphones",
    "unreadable"
]

prefixes = ["un", "re"]
suffixes = ["est", "ing", "able", "s"]

for word in words:
    original = word
    parts = []

    for p in prefixes:
        if word.startswith(p):
            parts.append(p)
            word = word[len(p):]
            break

    for s in suffixes:
        if word.endswith(s):
            word = word[:-len(s)]
            parts.append(s)
            break

    parts.insert(len(parts) if parts else 0, word)

    print(original, "->", " + ".join(parts))
