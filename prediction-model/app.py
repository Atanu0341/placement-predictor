import streamlit as st
import numpy as np
import pickle

# Load the trained model
pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

# Streamlit app
st.title("Student Placement Prediction")

# Input fields for CGPA and IQ
cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("Enter IQ", min_value=50, max_value=200)

# Prediction button
if st.button("Predict Placement"):
    prediction = model.predict([[cgpa, iq]])
    if prediction[0] == 1:
        st.success("Congratulations! The model predicts that the student will be placed.")
    else:
        st.error("Unfortunately, the model predicts that the student will not be placed.")
