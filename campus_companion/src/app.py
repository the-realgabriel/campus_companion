import streamlit as st
from pages.home import home_page
from pages.budget import budget_page
from pages.timetable import timetable_page
from pages.activities import activities_page
from pages.chatbot import chatbot_page

# Set up the Streamlit app configuration
st.set_page_config(page_title="Campus Companion", page_icon="🎓", layout="wide")

# Initialize session state for page routing
if "page" not in st.session_state:
    st.session_state.page = "home"

# Page routing logic
page = st.session_state.page
if page == "home":
    home_page()
elif page == "budget":
    budget_page()
elif page == "timetable":
    timetable_page()
elif page == "activities":
    activities_page()
elif page == "chatbot":
    chatbot_page()

# Auto-save data on every rerun
# (Assuming data saving functions are defined in utils/persistence.py)
from utils.persistence import save_data

# Save data logic can be added here if needed