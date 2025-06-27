# 🛡️ Credit Card Fraud Detection Web App

A simple and interactive web application to predict fraudulent credit card transactions using a trained machine learning model.

## 🚀 Features

- 📊 Takes transaction input (time and amount)
- 🧠 Uses a pre-trained machine learning model to predict fraud
- ✅ Real-time result: "Legitimate" or "Fraudulent"
- 🖥️ Built using Streamlit for easy web deployment

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** – UI and frontend
- **scikit-learn** – Model building
- **pandas**, **numpy** – Data processing
- **joblib** – Model loading

---

## 📂 File Structure
📦 Fraud-Detection-Web-App
│
├── app.py # Main Streamlit app
├── fraud_model.pkl # Trained ML model (not included)
├── req.txt # Project dependencies
├── README.md # This file

yaml
Copy
Edit
## 🧪 How to Run the Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/YourUsername/Fraud-Detection-Web-App.git
   cd Fraud-Detection-Web-App
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r req.txt
Run the app

bash
Copy
Edit
streamlit run app.py

