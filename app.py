import streamlit as st
import numpy as np
import pandas as pd

import joblib



model = joblib.load("./log_model.pkl")


# App title
st.title("Diabetes Prediction App")

# Input form for the user to enter health data
st.subheader("Enter your health details")

# Create input fields for the user to enter data
glucose = st.number_input("Glucose Level", min_value=0, max_value=200, step=1)
bp = st.number_input("Blood Pressure", min_value=0, max_value=180, step=1)
SkinT = st.number_input("Skin Thickness",min_value=0,max_value=100,step =1)
insulin = st.number_input("Insulin Level", min_value=0, max_value=850, step=1)
bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, step=0.1)

age = st.number_input("Age", min_value=0, max_value=120, step=1)
# Convert inputs to a DataFrame (reshape for model prediction)
input_data = pd.DataFrame({
    'Glucose': [glucose],
    'BloodPressure': [bp],
    'SkinThickness':[SkinT],
    'Insulin': [insulin],
    'BMI': [bmi], 
    'Age': [age]
})

# Display a button to run prediction
if st.button("Predict Diabetes"):
    # Run the prediction using the model
    prediction = model.predict(input_data)  # Predict using the input data

    # Display the result
    if prediction[0] == 1:
        st.write("The model predicts that you may have diabetes.")
    else:
        st.write("The model predicts that you are unlikely to have diabetes.")
