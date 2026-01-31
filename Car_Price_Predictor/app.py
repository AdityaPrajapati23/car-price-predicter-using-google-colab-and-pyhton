import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("car_price_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🚗 Car Price Prediction System")

present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0)
kms = st.number_input("Kilometers Driven", min_value=0)
age = st.number_input("Car Age", min_value=0)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
trans = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner Type", [0, 1, 2, 3])

fuel = 2 if fuel == "Petrol" else 1 if fuel == "Diesel" else 0
seller = 0 if seller == "Dealer" else 1
trans = 0 if trans == "Manual" else 1

if st.button("Predict Price"):
    input_data = scaler.transform([[
        present_price,
        kms,
        fuel,
        seller,
        trans,
        owner,
        age
    ]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Car Price: ₹ {round(prediction * 100000, 2)}")