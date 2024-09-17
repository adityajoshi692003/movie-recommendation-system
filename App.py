import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

# Load the external CSS file --------------------------------------------
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call the function to load the CSS
load_css("style.css")

# Code Starts Here ---------------------------------------------
def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distance)), reverse = True, key=lambda x: x[1])[1:6]


    recommended_movies = []

    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)  # Get the titles of the recommended movies


    return recommended_movies

similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommendations System')

selected_movie_name = st.selectbox(
    'Welcome To My Recommender System',
    movies['title'].values
)



if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.markdown(f"<p class='movie-title'>{movie}</p>", unsafe_allow_html=True)  # Apply animation class


