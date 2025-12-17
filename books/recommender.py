import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Set correct file path
CSV_PATH = os.path.join("C:/Users/DELL/Documents/book_recommendation_system/bookrec", "final_cleaned_books_updated2.csv")

# Load the dataset
books_df = pd.read_csv(CSV_PATH)

# Use only the book title for recommendations
books_df["combined_features"] = books_df["book_title"].astype(str)

# Convert text data into numerical vectors using TF-IDF
tfidf = TfidfVectorizer(stop_words="english", max_features=5000, ngram_range=(1, 2), min_df=2)
tfidf_matrix = tfidf.fit_transform(books_df["combined_features"])

# Fit Nearest Neighbors model (Cosine similarity)
nn_model = NearestNeighbors(n_neighbors=6, metric="cosine", algorithm="brute")
nn_model.fit(tfidf_matrix)


# Function to get similar books based on title
def get_similar_books(book_title, num_recommendations=5):
    matches = books_df[books_df["book_title"].str.lower().str.strip() == book_title.lower().strip()]
    if matches.empty:
        return []

    book_index = matches.index[0]
    distances, indices = nn_model.kneighbors(tfidf_matrix[book_index], n_neighbors=num_recommendations + 1)

    recommendations = []
    seen_titles = set()

    for idx, score in zip(indices[0][1:], distances[0][1:]):  # Skip the book itself
        if idx >= len(books_df):
            continue
        book_info = books_df.iloc[idx]
        book_title_rec = book_info["book_title"]
        if book_title_rec in seen_titles:
            continue
        recommendations.append({
            "title": book_info["book_title"],
            "author": book_info["book_author"],
            "publisher": book_info["publisher"],
            "similarity_score": round((1 - score) * 100, 2),
            "image_url": book_info["image_url"] or "/static/images/default-cover.jpg"
        })
        seen_titles.add(book_title_rec)
        if len(recommendations) == num_recommendations:
            break

    return recommendations
