import streamlit as st
import pickle
import numpy as np
import joblib

model = joblib.load("diabetes_model.pkl")

model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("🩺 Diabetes Prediction App")

preg = st.number_input("Pregnancies", 0, 20)
glucose = st.number_input("Glucose Level", 0, 200)
bp = st.number_input("Blood Pressure", 0, 150)
skin = st.number_input("Skin Thickness", 0, 100)
insulin = st.number_input("Insulin", 0, 900)
bmi = st.number_input("BMI", 0.0, 70.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
age = st.number_input("Age", 1, 100)

input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("❌ Diabetic")
    else:
        st.success("✅ Not Diabetic")
