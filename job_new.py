import streamlit as st
import pickle
import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
# company	employmenttype_jobstatus	jobdescription	jobid	joblocation_address	jobtitle	skills	job_tags	job_tags1
#recommend function
def recommend(movie):
        movie_index = data[data['jobtitle'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

        recommend_movies = []
        for i in movie_list:
            recommend_movies.append(data.iloc[i[0]][['company','employmenttype_jobstatus','joblocation_address','jobtitle','skills']])

        return recommend_movies

    
# Importing the dataset 
Job_dict = pickle.load(open('Job_recom.pkl','rb'))
data = pd.DataFrame(Job_dict)
similarity = pickle.load(open('job_similiar.pkl','rb'))


# Title of Page
st.title('Jobs Recommendation System')

select_movie_name = st.selectbox(
"How would you like to be contacted?",
data['jobtitle'].values)


#Button
if st.button('Recommend'):
    recommendations = recommend(select_movie_name)
    for i in recommendations:
        st.write(i) 

