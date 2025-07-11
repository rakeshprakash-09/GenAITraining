import streamlit as st

st.title("Sum Calculator: 1 to n")

n = st.number_input("Enter a positive integer n:", min_value=1, step=1, value=10)

if st.button("Calculate Sum"):
    total = 0
    for i in range(1, n + 1):
        total += i
    st.success(f"The sum of numbers from 1 to {n} is {total}.")

# Add a button to stop the Streamlit app
if st.button("Stop Application"):
    st.stop()
