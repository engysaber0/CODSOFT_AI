import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Using Content-Based Filtering
def load_movie_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Convert movie features to a format suitable for comparison
def create_feature_matrix(movies_data):
    descriptions = [', '.join(features) for features in movies_data.values()]
    vectorizer = TfidfVectorizer()
    feature_matrix = vectorizer.fit_transform(descriptions)
    return feature_matrix, vectorizer

def recommend_movie(user_input, feature_matrix, vectorizer, movies_data):
    user_features = vectorizer.transform([user_input])
    cosine_similarities = linear_kernel(user_features, feature_matrix).flatten()
    
    # Get top 5 matches
    indices = cosine_similarities.argsort()[-5:][::-1] 
    recommended = [list(movies_data.keys())[i] for i in indices]
    
    # Check if recommendations are empty
    if not recommended or cosine_similarities.max() == 0:
        return None
    
    return recommended

# Load the movie data
movies = load_movie_data('movies.json')
feature_matrix, vectorizer = create_feature_matrix(movies)

# Input genres from user
user_input = input("Enter your favorite genres or features: ")
recommended_movies = recommend_movie(user_input, feature_matrix, vectorizer, movies)

if recommended_movies is None:
    print("No matching movies found. Please try with different genres or features.")
else:
    print("Top recommendations:")
    for movie in recommended_movies:
        print(f" {movie} ")
