import streamlit as st
import sys

def calculate_average(scores):
    """Calculate the average of test scores"""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def determine_pass_fail(average, passing_threshold=60):
    """Determine if the average score is a pass or fail"""
    return "PASS" if average >= passing_threshold else "FAIL"

def main():
    st.set_page_config(
        page_title="Grade Average Calculator",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 Grade Average Calculator")
    st.markdown("---")
    
    # Sidebar for controls
    with st.sidebar:
        st.header("⚙️ Settings")
        passing_threshold = st.slider(
            "Passing Threshold (%)",
            min_value=0,
            max_value=100,
            value=60,
            help="Minimum average score required to pass"
        )
        
        st.markdown("---")
        st.header("🛑 Stop Application")
        if st.button("Stop Application", type="secondary"):
            st.success("Application stopped!")
            st.stop()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📝 Enter Test Scores")
        st.write("Enter 5 test scores (0-100):")
        
        # Input fields for test scores
        scores = []
        for i in range(5):
            score = st.number_input(
                f"Test {i+1} Score",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=0.1,
                key=f"score_{i}"
            )
            scores.append(score)
    
    with col2:
        st.header("📈 Results")
        
        if st.button("Calculate Average", type="primary"):
            # Calculate average
            average = calculate_average(scores)
            
            # Determine pass/fail
            result = determine_pass_fail(average, passing_threshold)
            
            # Display results
            st.metric("Average Score", f"{average:.2f}%")
            
            # Color-coded result
            if result == "PASS":
                st.success(f"🎉 Result: {result}")
            else:
                st.error(f"❌ Result: {result}")
            
            # Show individual scores
            st.subheader("📋 Individual Scores")
            for i, score in enumerate(scores):
                st.write(f"Test {i+1}: {score}%")
            
            # Show passing threshold
            st.info(f"Passing Threshold: {passing_threshold}%")
    
    # Additional features
    st.markdown("---")
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.subheader("📊 Statistics")
        if scores:
            st.write(f"Highest Score: {max(scores)}%")
            st.write(f"Lowest Score: {min(scores)}%")
            st.write(f"Score Range: {max(scores) - min(scores)}%")
    
    with col4:
        st.subheader("🎯 Performance")
        if scores:
            above_threshold = sum(1 for score in scores if score >= passing_threshold)
            st.write(f"Tests Above Threshold: {above_threshold}/5")
            st.write(f"Tests Below Threshold: {5 - above_threshold}/5")
    
    with col5:
        st.subheader("💡 Tips")
        st.write("• Aim for consistent scores")
        st.write("• Focus on improving weak areas")
        st.write("• Regular practice helps!")
    
    # Footer
    st.markdown("---")
    st.markdown("*Created with Streamlit*")
    
    # Keyboard shortcut info
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Keyboard Shortcuts:**")
    st.sidebar.markdown("• `Ctrl+C` - Stop the application")
    st.sidebar.markdown("• `R` - Refresh the page")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        st.info("Application stopped by user (Ctrl+C)")
        sys.exit(0)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.stop()
