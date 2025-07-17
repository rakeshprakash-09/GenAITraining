import streamlit as st

# Streamlit app config
st.set_page_config(page_title="Even or Odd Identifier", page_icon="🔢")
st.title("🔍 Even and Odd Number Identifier")
st.markdown("Enter a series of numbers separated by commas to see which are even and which are odd.")

# User input for numbers
input_numbers = st.text_input("📥 Enter numbers separated by commas (e.g. 1,2,3,4,5):")

if input_numbers:
    try:
        # Convert input string to a list of integers
        numbers = [int(num.strip()) for num in input_numbers.split(',')]

        # Separate even and odd numbers
        even_numbers = [num for num in numbers if num % 2 == 0]
        odd_numbers = [num for num in numbers if num % 2 != 0]

        # Display the results
        st.success(f"✅ Even numbers: {even_numbers}")
        st.info(f"🔷 Odd numbers: {odd_numbers}")

    except ValueError:
        st.error("❌ Please enter only integers separated by commas (e.g., 1, 2, 3)")

