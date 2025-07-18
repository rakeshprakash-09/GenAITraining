import streamlit as st

st.title("Word Reverser")

st.write("Enter a sentence below. Each word will be reversed, but the word order will remain the same.")

sentence = st.text_input("Enter your sentence:")

if sentence:
    reversed_words = ' '.join(word[::-1] for word in sentence.split())
    st.write("Reversed words:")
    st.success(reversed_words) 