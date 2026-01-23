import streamlit as st
import pandas as pd
import pickle

# Load model and preprocessor
model = pickle.load(open("artifacts/model.pkl", "rb"))
preprocessor = pickle.load(open("artifacts/preprocessor.pkl", "rb"))

st.title("Student Performance Prediction")

gender = st.selectbox("Gender", ["male", "female"])
ethnicity = st.selectbox("Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parent_edu = st.selectbox("Parental Education", [
    "some high school", "high school", "some college",
    "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation", ["none", "completed"])
math = st.number_input("Math Score", 0, 100, 50)
reading = st.number_input("Reading Score", 0, 100, 50)
writing = st.number_input("Writing Score", 0, 100, 50)

if st.button("Predict"):
    input_df = pd.DataFrame([[gender, ethnicity, parent_edu, lunch, test_prep, math, reading, writing]],
                            columns=[
                                "gender", "race/ethnicity", "parental level of education",
                                "lunch", "test preparation course",
                                "math score", "reading score", "writing score"
                            ])

    data = preprocessor.transform(input_df)
    result = model.predict(data)

    st.success(f"Predicted Score: {result[0]:.2f}")
