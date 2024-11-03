import streamlit as st
import pickle
import pandas as pd
import requests

# fetch poster from api
# api_key:34976bfa74ec83eb8291471d5371ce1b
# https://api.themoviedb.org/3/movie/{movie_id}?api_key=34976bfa74ec83eb8291471d5371ce1b&language=en-US

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=34976bfa74ec83eb8291471d5371ce1b&language=en-US")
    data = response.json()
    
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    

def recommend(movie):
    if movie not in movies['title'].values:
        raise ValueError("Movie title not found in the dataset")
    
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x : x[1])[1:6]

    recommended_movies =[]
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetching recommended movies
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetching recommended posters from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster
    
    
movies_dict = pickle.load(open('attributes/movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('attributes/similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie that you like',movies['title'].values)

if st.button('Recommend'):
    try:
        names,posters = recommend(selected_movie_name)
        col1,col2,col3,col4,col5 = st.columns(5)
        
        with col1:
            st.text(names[0])
            st.image(posters[0])
        
        with col2:
            st.text(names[1])
            st.image(posters[1])
        
        with col3:
            st.text(names[2])
            st.image(posters[2])
            
        with col4:
            st.text(names[3])
            st.image(posters[3])

        with col5:
            st.text(names[4])
            st.image(posters[4])
        
    
    except ValueError as e:
        st.error(str(e))
        
         