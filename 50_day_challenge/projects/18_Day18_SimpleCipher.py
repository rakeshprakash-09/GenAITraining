import streamlit as st

def shift_letters(word: str, shift: int = 1) -> str:
    """Shifts each letter in a word by the specified number of positions in the alphabet."""
    result = ""
    for char in word:
        if char.isalpha():
            # Determine the base (a=97, A=65)
            base = ord('a') if char.islower() else ord('A')
            # Calculate the shifted position
            shifted_pos = (ord(char) - base + shift) % 26
            # Convert back to character
            result += chr(base + shifted_pos)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

st.title("Simple Cipher")
st.write("Enter a word to shift each letter by 1 position in the alphabet.")

word_input = st.text_input("Enter a word:", "")

if word_input:
    shifted_word = shift_letters(word_input)
    st.success(f"Original: {word_input}")
    st.success(f"Shifted: {shifted_word}")
else:
    st.info("Please enter a word above.") 