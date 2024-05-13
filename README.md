
# Data Analytics 2024 - Project 4 - Open University Machine Learning Project
Team Members - Tyson Horsewell, Patric Beaven, Vijay Mani, Hail Nijo

## Overview:
By looking into Open University Data Student Data, we aim to create a model that can be used to answer questions regarding this data and develop relationships

## Aim
Get a general understanding of the data. (Total students, gender ratio, geography of students).
Then use machine learning the following questions:
1. Are there factors that cause some students to be more prone to dropping out than others?
2. Does IMBD_BAND affect the success of the student?
     - Logistic Regression
     - Decision Tree model
     - Deep Learning Model
     - Neural Network
3. How does Student interaction affect the final score?
     - Deep Learning Model
     
## Technologies Used
    - SQLite - Portable database allowing everyone to use the same database small and fast
    - Jupyter Notebooks - Easy to code, test and iterate
    - SQLAlchemy - Connect to SQLite to create and query the database
    - Pandas and Matplotlib - Analysis and Visualization
    - SkLearn and Tensorflow - Machine learning
    - Streamlit & Pandasai - App development
     
## Data Cleanup and Analysis
create_db.ipynb was used to turn the 6 csv's that contained data into an SQL Database. From there, the database can be accessed to make pandas dataframes and then analysis can begin.
This includes:
- Merging Dataframes together


1. Basic Data Overview:
   - 32,593 instances of students joining a course. 28, 785 being completely unique students (Unique Student ID's)
   - Students come from 13 different Regions with Scotland being the region with the most students and Ireland being the least
  (Insert Graph)
   - There are slightly more Male students over Female students. With 17,875 males students vs 14,718 students.
   (Insert Graph)
   - Passing is the highest "Final Result", however if you combine Passing with Distinction and Withrdrawal with Failing. Then Failing is higher.
   - (Insert graph)
   - 

1. Are there factors that cause some students to be more prone to dropping out than others?
   
2. Does IMD_BAND affect the success of the student?
    - IMD Band definition: Indices of multiple deprivation (IMD) are widely-used datasets within the UK to classify the relative deprivation of small areas.
    - Target to measure success is whether the student passed or failed
    - Features in each stage of the models:
    ![Feature Stages](images/model_stage_features.png)
    - Model Accuracy over the stages 
    ![Model Graph](images/model_accuracy.png)
    - Conclusion 
        - Multiple features impacted student success
        - Only focusing on IMD Band to predict if a student would pass or fail a course resulted in low accuracy models
        - Top three important features
         - Number of clicks with class material
         - Assessment scores
         - Date of registration
        - Most Successful Model 
        ![Random Forest](images/random_forest_model.png)

3. How does Student interaction affect the final score?

## Github Description


## Instructions for Web App
The web app has interactive tabs called Explore Data and Prediction Calculator. The first welcome page details an overview of our project and explains the models that were used to answer our questions for the dataset we analysed. The Explore Data page allows the user to query the dataset used for analysis through a chatbot. The user can ask the chatbot to plot graphs and answer basic questions questions about the university dataset. The Prediction Calculator page utilises a Random Forest model, the user can change feature inputs about a student and the model will predict whether the student will pass or fail the course.

## References & Datasets
https://www.kaggle.com/datasets/mexwell/open-university-learning-analytics
https://docs.streamlit.io/
https://docs.pandas-ai.com/en/latest/
https://scikit-learn.org/stable/


