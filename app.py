import streamlit as st
import pickle as pkl
import pandas as pd
import requests

# This is a updated repositoru
movies_list = pkl.load(open('movies.pkl','rb'))

similarity = pkl.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_list)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a26271ecd026c544346c26084cd885aa&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
    
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_sorted = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_sorted:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    print(recommended_movies)
    return recommended_movies,recommended_movies_posters


# title of the website
st.title("Movie Recommendation System")

selected_movie = st.selectbox('How would you like to be connected? ',movies['title'].values)
        
        
if st.button('Recommend'):
    recommendations,posters = recommend(selected_movie)
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])
    # st.write(selected_movie)