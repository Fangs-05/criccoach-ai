import streamlit as st
import os
from database import init_db

st.set_page_config(
    page_title="CricCoach AI",
    layout="wide"
)

# Initialize Database
init_db()

# Load External CSS
def load_css(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# --- UI UPGRADE: Professional Material Icons instead of Emojis ---
# You can also just delete the 'icon' parameter entirely for no icons at all.
analyze_page = st.Page("pages/1_analyze.py", title="Analyze Form", icon=":material/sports_cricket:")
progress_page = st.Page("pages/2_progress.py", title="Personal Progress", icon=":material/monitoring:")
how_it_works_page = st.Page("pages/3_how_it_works.py", title="How It Works", icon=":material/info:")
academy_page = st.Page("pages/4_academy.py", title="Academy Dashboard", icon=":material/groups:") # New Page

import streamlit as st

# --- THE MASTER TOGGLE ---
if 'app_mode' not in st.session_state:
    st.session_state.app_mode = "Batting 🏏"

st.sidebar.markdown("### ⚙️ App Context")
st.session_state.app_mode = st.sidebar.radio(
    "Select Discipline Mode:", 
    ["Batting 🏏", "Bowling ⚾"],
)
st.sidebar.divider()
# -------------------------

pg = st.navigation([analyze_page, progress_page, academy_page, how_it_works_page])
pg.run()