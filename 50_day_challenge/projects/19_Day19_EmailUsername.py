import streamlit as st

def extract_username(email):
    if '@' in email:
        return email.split('@')[0]
    return ''

st.title('Email Username Extractor')

email = st.text_input('Enter your email address:')

if email:
    username = extract_username(email)
    if username:
        st.success(f'Username: {username}')
    else:
        st.error('Invalid email address. Please enter a valid email.') 