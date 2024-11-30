import streamlit as st
from dotenv import load_dotenv
from eventhub_receiver import run
import asyncio

# Load environment variables
load_dotenv()

# Streamlit app
st.title("Bank Transaction Demo")

# Input fields for transaction details
st.header("Enter Transaction Details")

email = st.text_input("Email")
account_number = st.text_input("Account Number", value = 100)
transaction_type = st.selectbox("Transaction Type", ["Deposit", "Withdrawal"])
amount = st.number_input("Amount", min_value=0.0, step=0.01)

# Button to submit transaction
if st.button("Submit Transaction"):
    asyncio.run(run(email))