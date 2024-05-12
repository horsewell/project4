import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier


st.title('University Result Prediction')

st.divider()

st.write('This is a simple web app to predict the result of a student based on their demographics and interactions with course work')

st.divider()

st.sidebar.header('User Input Features')

#create function to get user input
def user_input_features():
    score = st.sidebar.slider('Score', min_value=0, max_value=1000, value=0)
    clicks = st.sidebar.slider('Clicks', min_value=1, max_value=28507, value=1)
    registration = st.sidebar.slider('Registration Date', min_value=-320, max_value=6, value=0)
    code_module = st.sidebar.selectbox('Module', ['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III'])
    region = st.sidebar.selectbox('Region', ['Scotland', 'East Anglian Region', 'London Region', 'South Region', 'North Western Region', 'West Midlands Region', 'South West Region', 'East Midlands Region', 'South East Region', 'Wales', 'Yorkshire Region', 'North Region', 'Ireland'])
    highest_education = st.sidebar.selectbox('Highest Education', ['No Formal quals', 'Lower Than A Level', 'A Level or Equivalent', 'HE Qualification', 'Post Graduate Qualification'])
    imd_band = st.sidebar.selectbox('IMD Band', ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%'])
    age_band = st.sidebar.selectbox('Age Band', ['0-35', '35-55', '55'])
    gender = st.sidebar.selectbox('Gender', ['M', 'F'])
    num_of_prev_attempts = st.sidebar.slider('Number of Previous Attempts', min_value=0, max_value=6, value=0)
    studied_credits = st.sidebar.slider('Studied Credits', min_value=30, max_value=630, value=30)
    disability = st.sidebar.selectbox('Disability', ['Y', 'N'])
    data = {'Score': score,
            'Clicks': clicks,
            'Registration Date': registration,
            'Module': code_module,
            'Region': region,
            'Highest Education': highest_education,
            'IMD Band': imd_band,
            'Age Band': age_band,
            'Gender': gender,
            'Number of Previous Attempts': num_of_prev_attempts,
            'Studied Credits': studied_credits,
            'Disability': disability}
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()

#combine user input with the entire dataset
df = pd.read_pickle('import_df.pkl')
df_drop = df.drop(columns=['Final Result'])
df_combined = pd.concat([input_df, df_drop], axis=0)

#Encode no binary columns
encode = ['Module', 'Region', 'Highest Education', 'IMD Band', 'Age Band', 'Gender', 'Disability']
for col in encode:
    dummy = pd.get_dummies(df_combined[col], prefix=col)
    df_combined = pd.concat([df_combined, dummy], axis=1)
    del df_combined[col]
df_combined = df_combined[:1]

#Display the user input features
st.subheader('User Input Features')

st.write(df_combined)

#Load the saved model
load_model = pickle.load(open('model.pkl', 'rb'))

#make predictions
prediction = load_model.predict(df_combined)
prediction_proba = load_model.predict_proba(df_combined)

st.subheader('Prediction')
student_result = np.array(['Fail', 'Pass'])
st.write(student_result[prediction])

st.subheader('Predicton Probability')
st.write(prediction_proba)


