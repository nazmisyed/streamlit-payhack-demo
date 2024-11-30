import streamlit as st
from dotenv import load_dotenv
from eventhub_receiver import run
import asyncio

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

    with st.expander("Other Settings"):
        transaction_date_time = st.text_input("Transaction Date Time", "23/2/2019 1:49")
        bank_account_num = st.number_input("Bank Account Number", value=0.33812389808911114)
        merchant = st.number_input("Merchant", value=0.5707617147015313)
        amt = st.number_input("Amount", value=1069.04)
        resident_name = st.number_input("Resident Name", value=0.33812389808911114)
        street = st.number_input("Street", value=0.33812389808911114)
        city = st.number_input("City", value=0.33812389808911114)
        lat = st.number_input("Latitude", value=32.5104)
        long = st.number_input("Longitude", value=-86.8138)
        city_pop = st.number_input("City Population", value=1089)
        job = st.number_input("Job", value=0.5148469490314066)
        trans_num = st.text_input("Transaction Number", "e76330ed3fa261d1483617da75edb200")
        unix_time = st.number_input("Unix Time", value=1329961758)
        transaction_latitude = st.number_input("Transaction Latitude", value=33.223426)
        transaction_longitude = st.number_input("Transaction Longitude", value=-87.809106)
        transaction_date = st.text_input("Transaction Date", "23/2/2019")
        transaction_time = st.text_input("Transaction Time", "1:49:18")
        hour = st.number_input("Hour", value=1)
        is_weekend = st.selectbox("Is Weekend", [0, 1], index=1)
        distance_from_transaction = st.number_input("Distance From Transaction", value=122.17607779493581)
        age = st.number_input("Age", value=53)
        is_senior = st.selectbox("Is Senior", [0, 1], index=0)
        gender_M = st.selectbox("Gender (Male)", [0, 1], index=0)
        
        # Category Inputs
        category_food_dining = st.selectbox("Category: Food Dining", [0, 1], index=0)
        category_gas_transport = st.selectbox("Category: Gas Transport", [0, 1], index=0)
        category_grocery_net = st.selectbox("Category: Grocery Net", [0, 1], index=0)
        category_grocery_pos = st.selectbox("Category: Grocery POS", [0, 1], index=0)
        category_health_fitness = st.selectbox("Category: Health Fitness", [0, 1], index=0)
        category_home = st.selectbox("Category: Home", [0, 1], index=0)
        category_kids_pets = st.selectbox("Category: Kids Pets", [0, 1], index=0)
        category_misc_net = st.selectbox("Category: Misc Net", [0, 1], index=0)
        category_misc_pos = st.selectbox("Category: Misc POS", [0, 1], index=0)
        category_personal_care = st.selectbox("Category: Personal Care", [0, 1], index=0)
        category_shopping_net = st.selectbox("Category: Shopping Net", [0, 1], index=0)
        category_shopping_pos = st.selectbox("Category: Shopping POS", [0, 1], index=0)
        category_travel = st.selectbox("Category: Travel", [0, 1], index=1)
    
        # Transaction Day Inputs
        transaction_day_Monday = st.selectbox("Transaction Day: Monday", [0, 1], index=0)
        transaction_day_Saturday = st.selectbox("Transaction Day: Saturday", [0, 1], index=0)
        transaction_day_Sunday = st.selectbox("Transaction Day: Sunday", [0, 1], index=1)
        transaction_day_Thursday = st.selectbox("Transaction Day: Thursday", [0, 1], index=0)
        transaction_day_Tuesday = st.selectbox("Transaction Day: Tuesday", [0, 1], index=0)
        transaction_day_Wednesday = st.selectbox("Transaction Day: Wednesday", [0, 1], index=0)

# Button to submit transaction
    if st.form_submit_button("Submit Transaction"):
        eventhub_dict = {
            "transaction_date_time": transaction_date_time,
            "bank_account_num": bank_account_num,
            "merchant": merchant,
            "amt": amt,
            "resident name": resident_name,
            "street": street,
            "city": city,
            "lat": lat,
            "long": long,
            "city_pop": city_pop,
            "job": job,
            "trans_num": trans_num,
            "unix_time": unix_time,
            "transaction_latitude": transaction_latitude,
            "transaction_longitude": transaction_longitude,
            "transaction_date": transaction_date,
            "transaction_time": transaction_time,
            "hour": hour,
            "is_weekend": is_weekend,
            "distance_from_transaction": distance_from_transaction,
            "age": age,
            "is_senior": is_senior,
            "gender_M": gender_M,
            "category_food_dining": category_food_dining,
            "category_gas_transport": category_gas_transport,
            "category_grocery_net": category_grocery_net,
            "category_grocery_pos": category_grocery_pos,
            "category_health_fitness": category_health_fitness,
            "category_home": category_home,
            "category_kids_pets": category_kids_pets,
            "category_misc_net": category_misc_net,
            "category_misc_pos": category_misc_pos,
            "category_personal_care": category_personal_care,
            "category_shopping_net": category_shopping_net,
            "category_shopping_pos": category_shopping_pos,
            "category_travel": category_travel,
            "transaction_day_Monday": transaction_day_Monday,
            "transaction_day_Saturday": transaction_day_Saturday,
            "transaction_day_Sunday": transaction_day_Sunday,
            "transaction_day_Thursday": transaction_day_Thursday,
            "transaction_day_Tuesday": transaction_day_Tuesday,
            "transaction_day_Wednesday": transaction_day_Wednesday,
            "email": email
        }
        print(eventhub_dict)
        # asyncio.run(run(email))
        # st.success("Transaction details submitted successfully.")