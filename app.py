import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('salary_model.pkl')

# Streamlit app
st.title("Salary Prediction App")

# Input for Years of Experience
years_experience = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=20.0, step=0.1)

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict(np.array([[years_experience]]))
    st.success(f"The predicted salary is: ${prediction[0]:,.2f}")
