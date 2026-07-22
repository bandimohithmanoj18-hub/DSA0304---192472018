import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = input("Enter a sentence: ").strip()

if not text:
    print("Input cannot be empty.")
else:
    try:
        tokens = word_tokenize(text)
        tagged_words = pos_tag(tokens)

        print("\nTokens:")
        print(tokens)

        print("\nMorphological Analysis:")
        print("-" * 30)
        print("{:<15}{}".format("Word", "POS Tag"))
        print("-" * 30)

        for word, tag in tagged_words:
            print("{:<15}{}".format(word, tag))

    except LookupError:
        print("Required NLTK resources are not installed.")
        print("Run:")
        print("python -m nltk.downloader punkt")
        print("python -m nltk.downloader punkt_tab")
        print("python -m nltk.downloader averaged_perceptron_tagger")
        print("python -m nltk.downloader averaged_perceptron_tagger_eng")