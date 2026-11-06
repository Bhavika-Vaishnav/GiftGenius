import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_gifts():
    """Load gift data from the CSV file."""
    gifts = pd.read_csv("data/gifts.csv")
    return gifts


def recommend_gifts(recipient, interests, occasion, budget):
    """Recommend gifts based on user preferences."""

    gifts = load_gifts()

    # Filter gifts within the user's budget
    gifts = gifts[gifts["price"] <= budget].copy()

    if gifts.empty:
        return gifts

    # Prepare gift information for comparison
    gifts["features"] = (
        gifts["recipient"].fillna("").str.replace(";", " ")
        + " "
        + gifts["interests"].fillna("").str.replace(";", " ")
        + " "
        + gifts["occasion"].fillna("")
    )

    # Prepare the user's preferences
    user_preferences = (
        recipient + " " + " ".join(interests) + " " + occasion
    )

    # Convert text into numerical values
    vectorizer = TfidfVectorizer()

    gift_vectors = vectorizer.fit_transform(gifts["features"])

    user_vector = vectorizer.transform([user_preferences])

    # Calculate similarity scores
    scores = cosine_similarity(user_vector, gift_vectors)[0]

    # Add match percentage
    gifts["match_percentage"] = (scores * 100).round(2)

    # Sort gifts by best match
    gifts = gifts.sort_values(
        by="match_percentage",
        ascending=False
    )

    return gifts