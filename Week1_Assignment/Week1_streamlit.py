import streamlit as st
import requests

st.set_page_config(page_title="Explain Like I'm 5", page_icon="🧸")
st.title("🧠 ELI5: Explain Like I'm 5")
st.markdown("Enter any topic below and get a super simple explanation, like you're 5 years old!")

topic = st.text_input("🔍 What do you want to understand?", placeholder="e.g., Black holes, Gravity, Blockchain")
temperature = st.slider("🎨 Creativity Level (0 = factual, 1 = creative)", 0.0, 1.0, 0.7)

if st.button("Explain it to me!"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Thinking like a 5-year-old genius..."):
            try:
                endpoint = "https://api.together.xyz/inference"
                headers = {"Authorization": "Bearer Key to be entered"}
                payload = {
                    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                    "prompt": f"Explain the topic '{topic}' in the simplest possible way, like you're explaining it to a 5-year-old.",
                    "temperature": temperature,
                    "max_tokens": 300
                }
                response = requests.post(endpoint, headers=headers, json=payload)
                if response.status_code == 200:
                    explanation = response.json().get("output", "No explanation returned.")
                    st.success("Here's your explanation:")
                    st.markdown(f"### 📘 {topic}\n{explanation}")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
