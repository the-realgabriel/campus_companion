import streamlit as st

def chatbot_page():
    st.title("🤖 StudyBot")
    st.info("Ask StudyBot a study question — currently a simple helper (no AI integration).")
    q = st.text_input("Ask StudyBot:")
    if q:
        st.markdown("**StudyBot says:**")
        if "assignment" in q.lower() or "due" in q.lower():
            st.write("Make a checklist, break the task into 25-minute pomodoro sessions, and set small milestones.")
        elif "budget" in q.lower() or "money" in q.lower():
            st.write("Track all incomes and expenses for 2 weeks to find savings opportunities. Use categories.")
        else:
            st.write("Good question! Try splitting it into smaller parts — what specifically would you like help with?")