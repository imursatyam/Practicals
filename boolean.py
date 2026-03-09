from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def boolean_retrieval(corpus, query):
    vectorizer = CountVectorizer(binary=True)
    X = vectorizer.fit_transform(corpus)
    
    # Create a simple table (Matrix)
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    q = query.lower()

    if " and " in q:
        w1, w2 = q.split(" and ")
        res = df[(df[w1] == 1) & (df[w2] == 1)].index
    elif " or " in q:
        w1, w2 = q.split(" or ")
        res = df[(df[w1] == 1) | (df[w2] == 1)].index
    elif "not " in q:
        w = q.split("not ")[1]
        res = df[df[w] == 0].index

    print(f"Query: {query} -> Result: {[i+1 for i in res]}")

# Example
corpus_bool = [
    "The cat chased the dog around the garden",
    "She was sitting in the garden last night",
    "I read the book the night before"
]
boolean_retrieval(corpus_bool, "garden or night")
