# Q3: Deleted Interpolation

lambda1 = 0.5
lambda2 = 0.3
lambda3 = 0.2

trigram = 2 / 3
bigram = 2 / 3
unigram = 2 / 15

probability = (lambda1 * trigram) + \
              (lambda2 * bigram) + \
              (lambda3 * unigram)

print("QUESTION 3")
print("--------------------")
print("Trigram Probability =", round(trigram, 3))
print("Bigram Probability =", round(bigram, 3))
print("Unigram Probability =", round(unigram, 3))
print("Final Probability =", round(probability, 2))
