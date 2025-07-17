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

# ---- App Header ----
st.title("🏁 50-Day Python Challenge")
st.markdown("""
Welcome to the **50-Day Python Mini Projects Challenge** built using Streamlit!  
Each day focuses on solving a mini problem to improve Python and Streamlit skills.

Use the sidebar to navigate through each day's challenge.

---
""")

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
st.subheader("📈 Progress Overview")
st.write(f"**{completed_days} out of {total_days} days completed ({progress_percent}%)**")

st.progress(progress_percent / 100)

# ---- Sidebar Navigation (Dropdown Only) ----
page_options = ["🏠 Main Page"] + [f"Day {f.split('_')[0]}: {f.split('_', 2)[2][:-3].replace('_', ' ')}" for f in project_files]
selected_page = st.sidebar.selectbox("Select a project", page_options, key="page_select")

def go_home():
    st.query_params["page"] = "main"
    st.session_state["page_select"] = "🏠 Main Page"

if selected_page == "🏠 Main Page":
    # Main page content (already shown above)
    pass
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
