from collections import Counter
import math

train = "the student is reading a book the student is learning"
test = "the student is reading"

w = train.split()
u = Counter(w)
total = len(w)

entropy = 0
count = 0

for word in test.split():
    p = u[word] / total

    if p > 0:
        entropy += -math.log2(p)
        count += 1

entropy = entropy / count

print("Test sentence:", test)
print("Entropy =", round(entropy, 3))
