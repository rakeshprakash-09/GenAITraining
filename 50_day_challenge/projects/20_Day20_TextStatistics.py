import streamlit as st
import re

st.title("Day 20: Text Statistics")

st.write("""
Enter a paragraph below to get the number of characters, words, and sentences it contains.
""")

text = st.text_area("Enter your paragraph here:", height=200)

if text:
    # Count characters (excluding leading/trailing whitespace)
    char_count = len(text)
    # Count words (split by whitespace)
    word_count = len(text.split())
    # Count sentences (split by '.', '!', '?')
    sentence_count = len(re.findall(r'[.!?]+', text))
    if text.strip() and not re.search(r'[.!?]$', text.strip()):
        # If the last sentence does not end with punctuation, count it
        sentence_count += 1

    st.subheader("Statistics:")
    st.write(f"**Characters:** {char_count}")
    st.write(f"**Words:** {word_count}")
    st.write(f"**Sentences:** {sentence_count}")
else:
    st.info("Please enter a paragraph above to see the statistics.") 