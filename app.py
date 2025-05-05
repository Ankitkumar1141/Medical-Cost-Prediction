import streamlit as st
import pandas as pd
import pickle

# Load the model and preprocessor
with open("best_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("preprocessor.pkl", "rb") as prep_file:
    preprocessor = pickle.load(prep_file)

# App title
st.title("Medical Insurance Cost Predictor")

# User inputs
age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["southeast", "southwest", "northeast", "northwest"])

# Prediction
if st.button("Predict Medical Cost"):
    # Create DataFrame from input
    input_data = pd.DataFrame(
        {
            "age": [age],
            "sex": [sex],
            "bmi": [bmi],
            "children": [children],
            "smoker": [smoker],
            "region": [region],
        }
    )

    # Preprocess input and predict
    transformed_data = preprocessor.transform(input_data)
    prediction = model.predict(transformed_data)

    # Display output in plain numeric format
    st.success(f"Estimated Medical Insurance Cost: ${prediction[0]:,.2f}")