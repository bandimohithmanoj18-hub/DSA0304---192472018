from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = [
    "I like machine learning.",
    "Machine learning is useful.",
    "The weather is sunny."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(text)

score = cosine_similarity(X[0:1], X[1:2])[0][0]

print("Coherence score:", score)
