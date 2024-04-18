import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_idx = movies[movies.title == movie].index[0]
    distances = similarity[movie_idx]
    movies_lst = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    rec_movies = []
    for i in movies_lst:
        movie_id = movies.iloc[i[0]].id

        rec_movies.append(movies.iloc[i[0]].title)

    return rec_movies


movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
"What movie did you like?",
movies.title.values)

if st.button("RECOMMEND"):
    for movie_name in recommend(selected_movie_name) :
        st.write(movie_name)