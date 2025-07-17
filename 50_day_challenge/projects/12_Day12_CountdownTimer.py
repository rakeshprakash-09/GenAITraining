import streamlit as st
import time

st.title("Countdown Timer")

# Session state for timer
if 'timer_running' not in st.session_state:
    st.session_state['timer_running'] = False
if 'remaining_time' not in st.session_state:
    st.session_state['remaining_time'] = 0

# Input for seconds
seconds = st.number_input("Enter countdown time in seconds:", min_value=1, value=10, step=1)

# Start and Stop buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Start"):
        st.session_state['timer_running'] = True
        st.session_state['remaining_time'] = seconds
with col2:
    if st.button("Stop"):
        st.session_state['timer_running'] = False

# Countdown logic
if st.session_state['timer_running']:
    if st.session_state['remaining_time'] > 0:
        with st.empty():
            for i in range(st.session_state['remaining_time'], 0, -1):
                if not st.session_state['timer_running']:
                    break
                st.write(f"Time left: {i} seconds")
                st.session_state['remaining_time'] = i
                time.sleep(1)
            else:
                st.session_state['timer_running'] = False
                st.session_state['remaining_time'] = 0
                st.write("Time's up!")
    else:
        st.session_state['timer_running'] = False
        st.write("Time's up!")
else:
    if st.session_state['remaining_time'] > 0:
        st.write(f"Time left: {st.session_state['remaining_time']} seconds")
    else:
        st.write("Timer stopped or not started.")

