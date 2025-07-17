import streamlit as st
import os
import runpy
import re

# ---- Page Config ----
st.set_page_config(
    page_title="50-Day Python Challenge",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Custom Styles ----
st.markdown(
    """
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        color: #FF6F61;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtitle {
        font-size: 1.3rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 1em;
    }
    .progress-label {
        font-size: 1.1rem;
        color: #1E90FF;
        font-weight: 600;
    }
    .challenge-banner {
        background: linear-gradient(90deg, #FFDEE9 0%, #B5FFFC 100%);
        border-radius: 12px;
        padding: 1.2em 1em 1em 1em;
        margin-bottom: 1.5em;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        color: #222 !important;
        font-size: 1.15rem;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- App Header ----
st.markdown('<div class="main-title">🏁 50-Day Python Challenge</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Welcome to the <b>50-Day Python Mini Projects Challenge</b> built using <span style="color:#FF6F61;">Streamlit</span>!<br>Each day focuses on solving a mini problem to improve your Python and Streamlit skills.</div>', unsafe_allow_html=True)

st.markdown('<div class="challenge-banner">🎯 <b>Goal:</b> Complete 50 fun and practical Python mini projects in 50 days!<br>🌈 <b>Tip:</b> Use the sidebar dropdown to explore each day\'s app.<br>✨ <b>Keep coming back for a new challenge every day!</b></div>', unsafe_allow_html=True)

# ---- Progress Calculation ----
projects_folder = "projects"
completed_days = 0

project_files = []
if os.path.exists(projects_folder):
    # Extract number prefix for sorting
    def extract_number(filename):
        match = re.match(r"(\d+)_", filename)
        return int(match.group(1)) if match else 0
    project_files = [
        file for file in os.listdir(projects_folder)
        if file.endswith(".py") and file[0].isdigit()
    ]
    project_files = sorted(project_files, key=extract_number)
    completed_days = len(project_files)

# Compute percentage
total_days = 50
progress_percent = int((completed_days / total_days) * 100)

# ---- Display Progress ----
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown('<div class="progress-label">📈 Progress Overview</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size:1.2rem; color:#FF6F61; font-weight:600; text-align:center;">{completed_days} out of {total_days} days completed <span style="color:#2E8B57;">({progress_percent}%)</span></div>', unsafe_allow_html=True)
    st.progress(progress_percent / 100)

# ---- Sidebar Navigation (Dropdown Only) ----
page_options = ["🏠 Main Page"] + [f"Day {f.split('_')[0]}: {f.split('_', 2)[2][:-3].replace('_', ' ')}" for f in project_files]
selected_page = st.sidebar.selectbox("Select a project", page_options, key="page_select")

def go_home():
    st.query_params["page"] = "main"
    st.session_state["page_select"] = "🏠 Main Page"

if selected_page == "🏠 Main Page":
    # Main page content (already shown above)
    st.markdown("""
    <div style='margin-top:2em; text-align:center;'>
        <span style='font-size:1.1rem;'>
        🚀 <b>How to Use:</b> Select a day from the sidebar to launch its mini app.<br>
        📅 <b>New project added every day!</b><br>
        📝 <b>Check your progress and revisit completed challenges anytime.</b>
        </span>
    </div>
    """, unsafe_allow_html=True)
else:
    # Find the corresponding file
    idx = page_options.index(selected_page) - 1
    project_file = project_files[idx]
    runpy.run_path(os.path.join(projects_folder, project_file))
    st.sidebar.markdown("---")
    st.sidebar.button("⬅️ Back to Main Page", on_click=go_home)

# ---- Optional Extras ----
with st.expander("💡 About This Challenge"):
    st.markdown("""
    - Each project is a self-contained mini app.
    - Files are organized in the `projects/` folder using Streamlit's multipage structure.
    - Challenges cover basics to advanced topics in Python and Streamlit.
    """)

st.info("Use the sidebar to select and explore each day's app.")
