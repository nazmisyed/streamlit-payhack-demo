import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit app
st.title("Bank Transaction Demo")

# Input fields for transaction details
st.header("Enter Transaction Details")
account_number = st.text_input("Account Number")
transaction_type = st.selectbox("Transaction Type", ["Deposit", "Withdrawal"])
amount = st.number_input("Amount", min_value=0.0, step=0.01)

# Button to submit transaction
if st.button("Submit Transaction"):
    if transaction_type == "Deposit":
        st.success(f"Successfully deposited ${amount} to account {account_number}.")
    elif transaction_type == "Withdrawal":
        st.success(f"Successfully withdrew ${amount} from account {account_number}.")
    else:
        st.error("Invalid transaction type.")