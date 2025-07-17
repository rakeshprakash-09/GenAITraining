import streamlit as st

st.title("Count Positive, Negative, and Zero Numbers")


numbers_str = st.text_input("Enter numbers separated by commas (e.g., 1, -2, 0, 5, -7):")

if numbers_str:
    try:
        numbers = [int(num.strip()) for num in numbers_str.split(",")]
        positives = sum(1 for n in numbers if n > 0)
        negatives = sum(1 for n in numbers if n < 0)
        zeros = sum(1 for n in numbers if n == 0)

        st.write(f"**Positive numbers:** {positives}")
        st.write(f"**Negative numbers:** {negatives}")
        st.write(f"**Zeros:** {zeros}")
    except ValueError:
        st.error("Please enter a valid list of integers separated by commas.")

st.info("To stop the app, press Ctrl+C in the terminal where Streamlit is running.")
