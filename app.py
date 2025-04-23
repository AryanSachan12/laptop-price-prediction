import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load pre-trained model pipeline
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Load sample data just to get feature names and options
df = pd.read_csv("./dataset/cleaned_laptop_data.csv")
X = df.drop("Price", axis=1)

# Set page title and header
st.set_page_config(page_title="Laptop Price Predictor", layout="wide")
st.title("💻 Laptop Price Predictor")
st.markdown("Enter laptop specifications to estimate the price:")

# Collect user input dynamically
user_input = {}

# Style customizations
input_style = """
    <style>
        .stNumberInput input {
            height: 35px;
            font-size: 16px;
            padding: 5px;
        }
        .stSelectbox select {
            height: 35px;
            font-size: 16px;
            padding: 5px;
        }
    </style>
"""

st.markdown(input_style, unsafe_allow_html=True)

# Loop through the columns to display the input fields
for col in X.columns:
    if X[col].dtype == "object":
        options = list(X[col].unique())
        user_input[col] = st.selectbox(
            col, options, key=col, help=f"Select the {col} of the laptop"
        )
    else:
        min_val = float(X[col].min())
        default = float(X[col].median())
        user_input[col] = st.number_input(
            col,
            min_value=min_val,
            value=default,
            key=col,
            help=f"Enter the {col} of the laptop",
        )

# Prediction button
if st.button("Predict Price"):
    input_df = pd.DataFrame([user_input])
    predicted_price = model.predict(input_df)[0]

    # Displaying the predicted price
    st.subheader(f"💰 Predicted Laptop Price: ₹ {predicted_price:,.2f}")
