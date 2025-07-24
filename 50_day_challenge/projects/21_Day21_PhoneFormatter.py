import streamlit as st

st.title("Phone Number Formatter")

phone_input = st.text_input("Enter a 10-digit phone number:")

if phone_input:
    digits_only = ''.join(filter(str.isdigit, phone_input))
    if len(digits_only) == 10:
        formatted = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
        st.success(f"Formatted Phone Number: {formatted}")
    else:
        st.error("Please enter exactly 10 digits.")