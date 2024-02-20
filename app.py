import streamlit as st 
import pandas as pd 
import pickle
import time

st.title("Movie Recommender System")

movies=pd.read_csv("datasets.csv")

similarity=pickle.load(open("similarity.pkl","rb"))
similarity=pd.DataFrame(similarity)

def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    movie_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x: x[1])[1:11]

    for i in movie_list:
        st.write(movies.iloc[i[0]].title)
        time.sleep(0.5)
        

selected_movie=st.selectbox(
"Select your Movie",
movies["title"].values)


if st.button("Recommend"):
    recommend(selected_movie)