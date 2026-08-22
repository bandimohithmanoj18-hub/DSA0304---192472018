import pandas as pd
import re
from nltk.stem import PorterStemmer
ps = PorterStemmer()
data = pd.read_csv("BBCNews.csv")
def stem_text(text):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return " ".join(ps.stem(word) for word in words)
data["Processed"] = data["Text"].fillna("").apply(stem_text)
print(data[["Text", "Processed"]].head())
