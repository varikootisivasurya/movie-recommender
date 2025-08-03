'''
Author: Bappy Ahmed
Modified by: Siva
Date: 2025-Aug-03
'''

import pickle
import streamlit as st
import requests
from src.utils.utils import fetch_poster

# TMDB API key
TMDB_API_KEY = "491d91b273a24193468205f0f4cba2ba"

# Function to fetch poster using TMDB API
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"
    except Exception as e:
        print(f"[ERROR] Failed to fetch poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/300x450?text=No+Image"


# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

# Streamlit UI setup
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title('🎬 Movie Recommender System Using Machine Learning')

# Load data
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "🎥 Type or select a movie from the dropdown",
    movie_list
)
# Function to fetch poster using movie title (searches TMDb)
def fetch_poster_by_title(title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data['results']:
            poster_path = data['results'][0].get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
        return "https://via.placeholder.com/300x450?text=No+Image"
    except Exception as e:
        print(f"[ERROR] Poster fetch failed for '{title}': {e}")
        return "https://via.placeholder.com/300x450?text=No+Image"

# Show recommendations on button click
if st.button('🔍 Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(recommended_movie_posters[i])
            st.caption(recommended_movie_names[i])
