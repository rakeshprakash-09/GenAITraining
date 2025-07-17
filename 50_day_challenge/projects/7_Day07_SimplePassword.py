import streamlit as st
import re

def check_password(password):
    errors = []
    # Length check
    if len(password) < 8:
        errors.append("Password must be minimum 8 characters long.")
    # Uppercase check
    if not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter.")
    # Should not start with a number
    if password and password[0].isdigit():
        errors.append("Password should not start with a number.")
    # Special character check
    if not any(c in '@#$' for c in password):
        errors.append("Password must contain at least one special character (@, #, $).")
    
    return errors


st.title("Simple Password Validator")

password = st.text_input("Enter password:", type="password")

if st.button("Check Password"):
    result = check_password(password)
    if not result:
        st.success("Password is valid.")
    else:
        st.error("Password is invalid:")
        for err in result:
            st.write(f"- {err}")
