import streamlit as st

st.title("Basic Calculator")


st.write("Enter two numbers and select an operation:")

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    num1 = st.number_input("First Number", value=0.0, format="%f", key="num1")
with col3:
    num2 = st.number_input("Second Number", value=0.0, format="%f", key="num2")
with col2:
    operation = st.selectbox("Operation", ["+", "-", "*", "/"], key="operation")

calculate = st.button("Calculate")

result = None
error = None

if calculate:
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                error = "Error: Division by zero is not allowed."
    except Exception as e:
        error = f"Invalid input: {e}"

    if error:
        st.error(error)
    else:
        st.success(f"Result: {num1} {operation} {num2} = {result}")
