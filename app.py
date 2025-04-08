import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained fraud detection model
model = joblib.load("fraud_model.pkl")

# Streamlit UI
st.title("Credit Card Fraud Detection")
st.write("Enter transaction details below to check if it's fraud or not.")

# User input fields
time = st.number_input("Time (seconds since first transaction)", min_value=0.0)
amount = st.number_input("Transaction Amount ($)", min_value=0.0)

# Placeholder for additional features
features = [time, amount] + [0] * 28  # Adding placeholder values for other features

if st.button("Check Fraud"):
    # Convert input to NumPy array and reshape
    input_data = np.array(features).reshape(1, -1)
    
    # Predict using the model
    prediction = model.predict(input_data)
    
    # Display result
    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Legitimate.")
