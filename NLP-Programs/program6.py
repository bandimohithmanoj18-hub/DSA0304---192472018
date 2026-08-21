import random

text = """
Natural language processing is a branch of artificial intelligence.
Natural language processing helps computers understand human language.
Artificial intelligence is transforming the world.
"""

words = text.lower().replace(".", "").split()

# Create bigram dictionary
bigram = {}

for i in range(len(words) - 1):
    key = words[i]
    value = words[i + 1]

    if key not in bigram:
        bigram[key] = []

    bigram[key].append(value)

# Generate text
word = random.choice(list(bigram.keys()))
generated = [word]

for i in range(20):
    if word in bigram:
        word = random.choice(bigram[word])
        generated.append(word)
    else:
        break

print("Generated Text:")
print(" ".join(generated))
