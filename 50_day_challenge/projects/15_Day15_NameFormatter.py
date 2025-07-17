import streamlit as st

st.title("Name Formatter")

st.write("Enter your full name to split it into first, middle, and second name.")

full_name = st.text_input("Full Name")

first_name = middle_name = second_name = ""

if full_name:
    parts = full_name.strip().split()
    if len(parts) == 2:
        first_name, second_name = parts
        middle_name = "(None)"
    elif len(parts) == 3:
        first_name, middle_name, second_name = parts
    else:
        st.warning("Please enter either two or three words for the name.")

    if len(parts) in [2, 3]:
        st.markdown(f"**First Name:** {first_name}")
        st.markdown(f"**Middle Name:** {middle_name}")
        st.markdown(f"**Second Name:** {second_name}")
