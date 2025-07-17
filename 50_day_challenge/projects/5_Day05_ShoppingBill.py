import streamlit as st

st.title("Shopping Bill Calculator")


st.write("Enter the cost of three items and the tax percentage to calculate the final amount.")

item1 = st.number_input("Enter the cost of item 1:", min_value=0.0, format="%f", step=0.01)
item2 = st.number_input("Enter the cost of item 2:", min_value=0.0, format="%f", step=0.01)
item3 = st.number_input("Enter the cost of item 3:", min_value=0.0, format="%f", step=0.01)
tax_percent = st.number_input("Enter the tax percentage:", min_value=0.0, format="%f", step=0.01)

if st.button("Calculate Final Amount"):
    total_cost = item1 + item2 + item3
    tax_amount = total_cost * (tax_percent / 100)
    final_amount = total_cost + tax_amount
    st.success(f"Final amount to be paid (including tax): {final_amount:.2f}")
