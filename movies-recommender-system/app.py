import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['Series_Title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].Series_Title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox('Choose your favourite movie.', movies['Series_Title'].values)


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    columns = st.columns(len(recommendations))
    for i, movie_title in enumerate(recommendations):
        poster_url = movies[movies['Series_Title'] == movie_title]['Poster_Link'].values
        if poster_url:
            columns[i].image(poster_url[0], caption=movie_title, width=125)

        else:
            columns[i].write(f'Poster not available for {movie_title}')
