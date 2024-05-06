import streamlit as st
import joblib
import numpy as np

st.title('University Result Prediction')

st.divider()

st.write('This is a simple web app to predict the result of a student based on their demographics.')

st.divider()

code_module = st.selectbox('Code Module', ['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III'])
region = st.selectbox('Region', ['Scotland', 'East Anglian Region', 'London Region', 'South Region', 'North Western Region', 'West Midlands Region', 'South West Region', 'East Midlands Region', 'South East Region', 'Wales', 'Yorkshire Region', 'North Region', 'Ireland'])
highest_education = st.selectbox('Highest Education', ['No Formal quals', 'Lower Than A Level', 'A Level or Equivalent', 'HE Qualification', 'Post Graduate Qualification'])
imd_band = st.selectbox('IMD Band', ['90-100%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '10-20%', '0-10%'])
age_band = st.selectbox('Age Band', ['0-35', '35-55', '55<='])
gender = st.selectbox('Gender', ['M', 'F'])
num_of_prev_attempts = st.number_input('Number of Previous Attempts', min_value=0, max_value=6, value=0)
studied_credits = st.number_input('Studied Credits', min_value=0, max_value=655, value=0)
disability = st.selectbox('Disability', ['Y', 'N'])

st.divider()

predict_button = st.button('Predict Result')

st.divider()

