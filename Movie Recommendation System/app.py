import numpy as np
import pandas as pd
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import string
import re

# Load dataset
netfix_df = pd.read_csv("netflixData.csv")

# Select required columns
required_nf_df = netfix_df[["Title", "Description", "Content Type", "Genres"]]

# Download stopwords
nltk.download("stopwords")

stemmer = nltk.SnowballStemmer("english")
stopword = set(stopwords.words("english"))


# ---------------- CLEAN FUNCTION ---------------- #
def clean(text):
    text = str(text).lower()

    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\w*\d\w*", "", text)

    text = [word for word in text.split() if word not in stopword]
    text = [stemmer.stem(word) for word in text]

    return " ".join(text)


# Apply cleaning
required_nf_df["Title"] = required_nf_df["Title"].apply(clean)

# TF-IDF on Genres
generelist = required_nf_df["Genres"].astype(str).tolist()

tfidf = text.TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(generelist)

# Cosine similarity
similarity = cosine_similarity(tfidf_matrix)

# Mapping index
indices = pd.Series(
    required_nf_df.index, index=required_nf_df["Title"]
).drop_duplicates()


# ---------------- RECOMMENDATION FUNCTION ---------------- #
def netflix_recommendation(title, similarity=similarity):
    title = clean(title)

    if title not in indices:
        return None

    Index = indices[title]

    similarity_scores = list(enumerate(similarity[Index]))

    # Sort by similarity (important improvement)
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Skip first one (itself)
    similarity_scores = similarity_scores[1:11]

    movieindices = [i[0] for i in similarity_scores]

    return required_nf_df.iloc[movieindices][["Title", "Genres"]]


# ---------------- USER INTERFACE ---------------- #
print("\n🎬 Netflix Recommendation System")
print("----------------------------------")

while True:
    user_input = input("\nEnter a movie title (or type 'exit'): ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    recommendations = netflix_recommendation(user_input)

    if recommendations is None:
        print("❌ Movie not found in dataset. Try another one.")
    else:
        print("\n✅ Top Recommendations:\n")
        for i, row in enumerate(recommendations.values, start=1):
            print(f"{i}. {row[0]}  |  {row[1]}")
