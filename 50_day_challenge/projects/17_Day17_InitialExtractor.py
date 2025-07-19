import streamlit as st

def extract_initials(name: str) -> str:
    """Extracts and returns the initials from a full name string."""
    # Split the name by whitespace, filter out empty parts, and take the first character of each part
    parts = [part for part in name.strip().split() if part]
    initials = ''.join([part[0].upper() for part in parts])
    return initials

st.title("Initial Extractor")
st.write("Enter your full name to get your initials.")

name_input = st.text_input("Full Name", "")

if name_input:
    initials = extract_initials(name_input)
    st.success(f"Your initials: {initials}")
else:
    st.info("Please enter your name above.") 