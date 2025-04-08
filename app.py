import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('fraud_model_u2.pkl')  # Load your saved model

st.title("Credit Card Fraud Detection System 💳")

st.write("Enter transaction details below to check if it's Fraud or Genuine")

# Input Features (Example based on your dataset features)
# Replace with your actual features
V1 = st.number_input("V1")
V2 = st.number_input("V2")
V3 = st.number_input("V3")
V4 = st.number_input("V4")
V5 = st.number_input("V5")
Amount = st.number_input("Amount")

if st.button("Predict"):
    # Make dataframe from user input
    input_data = pd.DataFrame([[V1, V2, V3, V4, V5, Amount]],
                               columns=['V1', 'V2', 'V3', 'V4', 'V5', 'Amount'])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Genuine Transaction")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
