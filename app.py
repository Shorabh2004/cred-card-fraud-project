import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('fraud_model_u2.pkl')  # Load your saved model

st.title("Credit Card Fraud Detection System 💳")

# Use the same feature names used during training
feature_names = model.feature_names_in_

# Take user input dynamically
user_input = []

for feature in feature_names:
    value = st.number_input(f'Enter {feature}')
    user_input.append(value)

if st.button('Predict'):
    # Convert to DataFrame with correct feature names
    input_data = pd.DataFrame([user_input], columns=feature_names)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Genuine Transaction")
