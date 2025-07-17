import streamlit as st

st.title("Personal Greeting App")


st.write("👋 Welcome! Let's get to know you better.")

name = st.text_input("What's your name?")
age = st.text_input("How old are you?")
favorite_color = st.text_input("What's your favorite color?")

if name and age and favorite_color:
    st.markdown("---")
    st.success(f"Hi {name}! 🌟 You're {age} years young and love the color {favorite_color}. That's awesome!")
    st.info("Have a colorful and amazing day! 🎉")
