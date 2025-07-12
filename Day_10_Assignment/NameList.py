import streamlit as st
import sys

def main():
    st.title("Name List Application")
    st.write("Enter 5 names and see their lengths!")
    
    # Initialize session state for names list
    if 'names' not in st.session_state:
        st.session_state.names = []
    
    # Input section
    st.header("Input Names")
    
    # Create input fields for 5 names
    name_inputs = []
    for i in range(5):
        name = st.text_input(f"Enter name {i+1}:", key=f"name_{i}")
        name_inputs.append(name)
    
    # Process button
    if st.button("Process Names"):
        # Clear previous names and add new ones
        st.session_state.names = [name.strip() for name in name_inputs if name.strip()]
        
        if len(st.session_state.names) == 5:
            st.success("All 5 names have been stored!")
        else:
            st.warning(f"Please enter all 5 names. Currently entered: {len(st.session_state.names)}")
    
    # Display section
    if st.session_state.names:
        st.header("Name List with Lengths")
        
        # Create a table to display names and their lengths
        data = {
            "Name": st.session_state.names,
            "Length": [len(name) for name in st.session_state.names]
        }
        
        st.table(data)
        
        # Display summary
        st.subheader("Summary")
        total_length = sum(len(name) for name in st.session_state.names)
        avg_length = total_length / len(st.session_state.names)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Names", len(st.session_state.names))
        with col2:
            st.metric("Total Characters", total_length)
        with col3:
            st.metric("Average Length", f"{avg_length:.1f}")
    
    # Stop button
    st.header("Application Control")
    if st.button("Stop Application", type="primary"):
        st.success("Application stopped!")
        st.stop()
    
    # Clear button
    if st.button("Clear Names"):
        st.session_state.names = []
        st.rerun()

if __name__ == "__main__":
    main()
