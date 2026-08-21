from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
    "machine learning is useful",
    "deep learning uses neural networks",
    "machine learning uses data"
]

query = ["machine learning"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs + query)

scores = cosine_similarity(X[-1], X[:-1])

for i, score in enumerate(scores[0]):
    print("Document", i + 1, score)
