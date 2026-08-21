from collections import Counter

text = "the student is reading a book the student is learning python"
w = text.split()

u = Counter(w)
b = Counter(zip(w,w[1:]))
t = Counter(zip(w,w[1:],w[2:]))

s = input("Enter sentence: ").split()
a, c = s[-2], s[-1]

print("\nPredictions:")

for word in u:
    p3 = t[(a,c,word)] / b[(a,c)] if b[(a,c)] else 0
    p2 = b[(c,word)] / u[c] if u[c] else 0
    p1 = u[word] / len(w)

    # Backoff
    backoff = p3 or p2 or p1

    # Interpolation
    interp = .5*p3 + .3*p2 + .2*p1

    print(word, "Backoff:", round(backoff,2),
          "Interpolation:", round(interp,2))
