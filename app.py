import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list = movies['title'].values

st.header("Movie Recommendation System")

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:11]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

selected_movie = st.selectbox(
    "Choose a movie",
    movies_list
)

if st.button("Show recommendations"):
    movies_name, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col1:
        st.text(movies_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movies_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movies_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movies_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movies_name[4])
        st.image(movie_poster[4])
    with col6:
        st.text(movies_name[5])
        st.image(movie_poster[5])
    with col7:
        st.text(movies_name[6])
        st.image(movie_poster[6])
    with col8:
        st.text(movies_name[7])
        st.image(movie_poster[7])
    with col9:
        st.text(movies_name[8])
        st.image(movie_poster[8])
    with col10:
        st.text(movies_name[9])
        st.image(movie_poster[9])
