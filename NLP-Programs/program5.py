from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

n = int(input("Enter number of words: "))

if n <= 0:
    print("Invalid Input")
else:
    print("\nStemmed Words")
    print("-" * 30)
    print("{:<20}{}".format("Original", "Stem"))
    print("-" * 30)

    for _ in range(n):
        word = input("Enter word: ").strip()

        if word:
            print("{:<20}{}".format(word, stemmer.stem(word)))
        else:
            print("{:<20}{}".format("Empty", "Invalid"))