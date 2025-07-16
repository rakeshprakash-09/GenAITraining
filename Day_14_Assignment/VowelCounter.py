import streamlit as st

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

st.title("Vowel Counter App")

st.write("Enter a word or sentence to count the number of vowels:")

user_input = st.text_input("Type here:")

if user_input:
    vowel_count = count_vowels(user_input)
    st.success(f"Number of vowels: {vowel_count}")
