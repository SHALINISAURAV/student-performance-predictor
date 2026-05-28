# Import required libraries
import streamlit as st
import pandas as pd
import joblib

from pathlib import Path
import sys


# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Add src folder to system path
sys.path.append(str(BASE_DIR / 'src'))

# Import utility function
from utils import performance_category


# Load trained model
model_path = BASE_DIR / 'models/model.pkl'

model = joblib.load(model_path)


# Streamlit App Title
st.title("Student Performance Predictor")

st.write("Enter student details to predict math score.")


# USER INPUTS

gender = st.selectbox(
    "Gender",
    ["female", "male"]
)

race_ethnicity = st.selectbox(
    "Race/Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "bachelor's degree",
        "some college",
        "master's degree",
        "associate's degree",
        "high school",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    ["standard", "free/reduced"]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading_score = st.slider(
    "Reading Score",
    0,
    100,
    50
)

writing_score = st.slider(
    "Writing Score",
    0,
    100,
    50
)


# MANUAL ENCODING

gender_map = {
    "female": 0,
    "male": 1
}

race_map = {
    "group A": 0,
    "group B": 1,
    "group C": 2,
    "group D": 3,
    "group E": 4
}

education_map = {
    "bachelor's degree": 0,
    "some college": 1,
    "master's degree": 2,
    "associate's degree": 3,
    "high school": 4,
    "some high school": 5
}

lunch_map = {
    "standard": 0,
    "free/reduced": 1
}

course_map = {
    "none": 0,
    "completed": 1
}


# PREDICTION BUTTON

if st.button("Predict Score"):

    # Create dataframe for prediction
    input_data = pd.DataFrame({

        "gender": [
            gender_map[gender]
        ],

        "race/ethnicity": [
            race_map[race_ethnicity]
        ],

        "parental level of education": [
            education_map[parental_level_of_education]
        ],

        "lunch": [
            lunch_map[lunch]
        ],

        "test preparation course": [
            course_map[test_preparation_course]
        ],

        "reading score": [
            reading_score
        ],

        "writing score": [
            writing_score
        ]

    })

    # Predict score
    prediction = model.predict(input_data)[0]

    # Show prediction
    st.success(
        f"Predicted Math Score: {prediction:.2f}"
    )

    # Get performance category
    category = performance_category(prediction)

    # Show category
    st.info(
        f"Performance Category: {category}"
    )