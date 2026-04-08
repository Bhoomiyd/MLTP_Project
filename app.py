import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("best_model.pkl", "rb"))

st.title("Weather Temperature Predictor")

st.write("Enter the weather parameters to predict the temperature:")

humidity = st.number_input("Humidity", min_value=0.0, max_value=100.0, value=50.0)
wind_speed = st.number_input("Wind Speed", min_value=0.0, value=5.0)
pressure = st.number_input("Pressure", min_value=900.0, max_value=1100.0, value=1013.0)
rainfall = st.number_input("Rainfall", min_value=0.0, value=10.0)

if st.button("Predict Temperature"):
    features = np.array([[humidity, wind_speed, pressure, rainfall]])
    prediction = model.predict(features)[0]
    st.write(f"Predicted Temperature: {prediction:.2f} °C")