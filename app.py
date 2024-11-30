import streamlit as st
from dotenv import load_dotenv
from eventhub_receiver import run
from global_model import global_model
import asyncio
import shap 
import matplotlib.pyplot as plt


st.set_page_config(layout = "wide")

# Load environment variables
load_dotenv()

# Streamlit app
st.title("Bank Transaction Demo")

# Input fields for transaction details
st.header("Transaction Detail")

with st.form("Enter Transaction Details"):
    col1, col2 = st.columns([5,5])

    with col1:
        email = st.text_input("email")
    with col2:
        amt = st.number_input("Amount", value=281.06, step=0.01)

    with st.expander("Other Settings"):
        trans_date_trans_time = st.text_input("Transaction Date & Time", "2019-01-02 01:06:37")
        cc_num = st.number_input("Credit Card Number", value=4613314721966, step=1)
        merchant = st.text_input("Merchant", "fraud_Rutherford-Mertz")
        category = st.selectbox("Category", ["grocery_pos", "misc_net", "food_dining", "travel", "shopping_net"], index=0)
        first = st.text_input("First Name", "Jason")
        last = st.text_input("Last Name", "Murphy")
        gender = st.selectbox("Gender", ["M", "F"], index=0)
        street = st.text_input("Street", "542 Steve Curve Suite 011")
        city = st.text_input("City", "Collettsville")
        state = st.text_input("State", "NC")
        zip_code = st.number_input("ZIP Code", value=28611, step=1)
        lat = st.number_input("Latitude", value=35.9946, format="%.6f")
        long = st.number_input("Longitude", value=-81.7266, format="%.6f")
        city_pop = st.number_input("City Population", value=885, step=1)
        job = st.text_input("Job", "Soil scientist")
        dob = st.text_input("Date of Birth", "1988-09-15")
        trans_num = st.text_input("Transaction Number", "e8a81877ae9a0a7f883e15cb39dc4022")
        unix_time = st.number_input("Unix Time", value=1325466397, step=1)
        merch_lat = st.number_input("Merchant Latitude", value=36.430124, format="%.6f")
        merch_long = st.number_input("Merchant Longitude", value=-81.179483, format="%.6f")


# Button to submit transaction
    if st.form_submit_button("Submit Transaction"):
        transaction_data = {
            "trans_date_trans_time": trans_date_trans_time,
            "cc_num": cc_num,
            "merchant": merchant,
            "category": category,
            "amt": amt,
            "first": first,
            "last": last,
            "gender": gender,
            "street": street,
            "city": city,
            "state": state,
            "zip": zip_code,
            "lat": lat,
            "long": long,
            "city_pop": city_pop,
            "job": job,
            "dob": dob,
            "trans_num": trans_num,
            "unix_time": unix_time,
            "merch_lat": merch_lat,
            "merch_long": merch_long,
            "email_address": email
        }

        asyncio.run(run(transaction_data))
        st.success("Transaction details submitted successfully.")

    with st.expander("SHAP Value"):
        
        shap_values, sample_data, explainer = global_model()
        fig_summary, ax_summary = plt.subplots()
        shap.summary_plot(shap_values, sample_data, show=False)
        st.pyplot(fig_summary)

        # Force Plot for a specific transaction
        st.subheader("SHAP Force Plot for a Sample Transaction")
        transaction_idx = st.selectbox("Select Transaction Index:", sample_data.index)
        # shap.force_plot(explainer.expected_value[1], shap_values[transaction_idx].values, sample_data.iloc[transaction_idx])
        st.pyplot()
