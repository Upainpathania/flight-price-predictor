import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt

# ================= LOAD MODEL =================
model = pickle.load(open("pipe.pkl", "rb"))

# ================= PAGE CONFIG =================
st.set_page_config(page_title="✈️ Flight Price Predictor", layout="wide")

# Title
st.markdown(
    """
    <h1 style='text-align: center;'>Flight price  preidctor</h1>
    <p style='text-align: center;'>Made by <b>Sukhmanpreet kaur</b></p>
    <hr>
    """,
    unsafe_allow_html=True
)
# ================= CUSTOM CSS =================
st.markdown("""
<style>
body {
    background-color: #020617;
}
.main {
    background: linear-gradient(135deg, #020617, #0f172a);
}
h1 {
    text-align: center;
    color: #00F5FF;
    font-size: 50px;
}
.stButton>button {
    background: linear-gradient(90deg, #00F5FF, #00FFA3);
    color: black;
    border-radius: 12px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}
.sidebar .sidebar-content {
    background-color: #020617;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("<h1>✈️ Flight Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Enter details and get instant prediction 🚀</p>", unsafe_allow_html=True)

# ================= ANIMATION =================
st.markdown("""
<h3 style='text-align:center;'>✈️ Smart AI Flight Engine ✈️</h3>
<marquee behavior="alternate" scrollamount="8">✈️ 💨 ✈️ 💨 ✈️ 💨 ✈️</marquee>
""", unsafe_allow_html=True)

# ================= SIDEBAR INPUT =================
st.sidebar.title("🎛️ Flight Inputs")

airline = st.sidebar.selectbox("Airline", [
    "IndiGo", "Air India", "Jet Airways", "SpiceJet", "Vistara", "GoAir"
])

source = st.sidebar.selectbox("Source", [
    "Delhi", "Kolkata", "Mumbai", "Chennai", "Banglore"
])

destination = st.sidebar.selectbox("Destination", [
    "Cochin", "Delhi", "New Delhi", "Hyderabad", "Kolkata"
])

stops = st.sidebar.selectbox("Total Stops", [0, 1, 2, 3])

date = st.sidebar.date_input("Journey Date")

# ================= DATE FEATURES =================
day = date.day
month = date.month
day_of_week = date.weekday()
is_weekend = 1 if day_of_week >= 5 else 0

# ================= MAIN BUTTON =================
if st.button("🚀 Predict Price"):

    input_df = pd.DataFrame({
        "Airline": [airline],
        "Source": [source],
        "Destination": [destination],
        "Total_Stops": [stops],
        "Additional_Info": ["No info"],
        "Journey_Day": [day],
        "Journey_Month": [month],
        "Journey_Day_of_Week": [day_of_week],
        "Is_Weekend": [is_weekend]
    })

    # ================= FEATURE ENGINEERING =================
    input_df['Duration_Hours'] = 2.5  
    input_df['Dep_Hour'] = 10
    input_df['Arrival_Hour'] = 12

    def get_part_of_day(hour):
        if 5 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 17:
            return 'Afternoon'
        elif 17 <= hour < 21:
            return 'Evening'
        else:
            return 'Night'

    input_df['Dep_Part_of_Day'] = input_df['Dep_Hour'].apply(get_part_of_day)
    input_df['Arrival_Part_of_Day'] = input_df['Arrival_Hour'].apply(get_part_of_day)
    input_df['Route_Popularity'] = 1

    # ================= PREDICTION =================
    try:
        price = np.exp(model.predict(input_df)[0])

        # ================= RESULT CARD =================
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #00F5FF, #00FFA3);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            color: black;
            font-size: 30px;
            font-weight: bold;
        ">
        💰 Estimated Price: ₹ {round(price, 2)}
        </div>
        """, unsafe_allow_html=True)

        # ================= PRICE INTELLIGENCE =================
        if price < 4000:
            st.success("🔥 Cheap Flight! Best time to book!")
        elif price < 8000:
            st.warning("⚡ Moderate Price — consider booking soon")
        else:
            st.error("💸 Expensive Flight — try different dates")

        # ================= VISUALIZATION =================
        st.subheader("📊 Price Range Analysis")

        prices = [price * 0.8, price, price * 1.2]
        labels = ["Low Estimate", "Predicted", "High Estimate"]

        fig, ax = plt.subplots()
        ax.bar(labels, prices)
        ax.set_ylabel("Price")
        ax.set_title("Predicted Price Range")

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
