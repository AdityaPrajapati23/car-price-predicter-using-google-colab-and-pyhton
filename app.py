import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("car_price_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

st.title("🚗 Car Price Prediction System")
st.write("Enter car details to predict the selling price")

present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0)
kms = st.number_input("Kilometers Driven", min_value=0)
age = st.number_input("Car Age (Years)", min_value=0)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
trans = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner Type", [0, 1, 2, 3])

# Convert categorical to numerical
fuel = 2 if fuel == "Petrol" else 1 if fuel == "Diesel" else 0
seller = 0 if seller == "Dealer" else 1
trans = 0 if trans == "Manual" else 1

if st.button("Predict Price"):
    input_data = scaler.transform([[present_price, kms, fuel, seller, trans, owner, age]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Car Price: ₹ {round(prediction, 2)} Lakhs")