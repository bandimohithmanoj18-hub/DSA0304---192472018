from collections import Counter

text = "the student is reading a book the student is learning python"
w = text.split()

uni = Counter(w)
bi = Counter(zip(w, w[1:]))
tri = Counter(zip(w, w[1:], w[2:]))

print("Unigram:", uni)
print("Bigram:", bi)
print("Trigram:", tri)

s = input("Enter sentence: ").split()
last = s[-1]

print("\nNext word predictions:")
for (a, b), c in bi.items():
    if a == last:
        print(b, "Probability =", round(c/uni[a], 2))

print("\nUnseen bigram probability = 0")
