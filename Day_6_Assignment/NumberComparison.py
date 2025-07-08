import streamlit as st

st.title("Number Comparison App")

num1 = st.number_input("Enter the first number:", format="%f")
num2 = st.number_input("Enter the second number:", format="%f")

if st.button("Compare"):
    if num1 > num2:
        st.success(f"{num1} is larger than {num2}.")
    elif num1 < num2:
        st.success(f"{num1} is smaller than {num2}.")
    else:
        st.info("Both numbers are equal.")
