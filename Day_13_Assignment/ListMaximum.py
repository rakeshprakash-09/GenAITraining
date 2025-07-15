import streamlit as st

st.title("Find the Largest Number in a List")

if 'stopped' not in st.session_state:
    st.session_state['stopped'] = False

if not st.session_state['stopped']:
    numbers_str = st.text_input("Enter numbers separated by commas:")
    if st.button("Find Largest"):
        try:
            numbers = [float(num.strip()) for num in numbers_str.split(',') if num.strip()]
            if numbers:
                largest = numbers[0]
                for num in numbers[1:]:
                    if num > largest:
                        largest = num
                st.success(f"The largest number is: {largest}")
            else:
                st.warning("Please enter at least one number.")
        except ValueError:
            st.error("Please enter valid numbers separated by commas.")
    if st.button("Stop App"):
        st.session_state['stopped'] = True
else:
    st.warning("The application has been stopped. Refresh the page to restart.")
