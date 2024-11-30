import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit app
st.title("Bank Transaction Demo")

# Input fields for transaction details
st.header("Enter Transaction Details")

transaction_date_time = st.text_input("Transaction Date Time")
bank_account_num = st.text_input("Bank Account Number")
merchant = st.text_input("Merchant")
amt = st.number_input("Amount", min_value=0.0, step=0.01)
resident_name = st.text_input("Resident Name")
street = st.text_input("Street")
city = st.text_input("City")
lat = st.number_input("Latitude", format="%.6f")
long = st.number_input("Longitude", format="%.6f")
city_pop = st.number_input("City Population", min_value=0)
job = st.text_input("Job")
trans_num = st.text_input("Transaction Number")
unix_time = st.number_input("Unix Time", min_value=0)
transaction_latitude = st.number_input("Transaction Latitude", format="%.6f")
transaction_longitude = st.number_input("Transaction Longitude", format="%.6f")
transaction_date = st.date_input("Transaction Date")
transaction_time = st.time_input("Transaction Time")
hour = st.number_input("Hour", min_value=0, max_value=23)
is_weekend = st.checkbox("Is Weekend")
distance_from_transaction = st.number_input("Distance from Transaction", min_value=0.0, step=0.01)
age = st.number_input("Age", min_value=0)
is_senior = st.checkbox("Is Senior")
gender_M = st.checkbox("Gender (Male)")

# Button to submit transaction
if st.button("Submit Transaction"):
    st.success("Transaction details submitted successfully.")