import streamlit as st
import pickle as pkl
import pandas as pd

movies_list = pkl.load(open('movies.pkl','rb'))

similarity = pkl.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommend_movies = []
    for i in movies:
        movie_id = i[0]
        # fetch poster from api
        recommend_movies.append(movies_list.iloc[i[0]].title)
    
    return recommend_movies


# title of the website
st.title("Movie Recommendation System")

selected_movie = st.selectbox('How would you like to be connected? ',movies_list['title'].values)
        
        
if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
    # st.write(selected_movie)