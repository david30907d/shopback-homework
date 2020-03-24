import json

from sklearn.feature_extraction.text import TfidfVectorizer


def q2(path:str="../question1/output.txt") -> None:
    with open(path, "r") as f:
        corpus = f.readlines()
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    json.dump(X.toarray().tolist(), open("output2.txt", "w"))
