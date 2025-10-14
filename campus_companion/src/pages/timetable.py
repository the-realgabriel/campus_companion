import streamlit as st
import datetime
import uuid
import json
import os
from config import FILES, DATA_DIR


# Filepath for data storage
DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

FILES = {
    "timetable": os.path.join(DATA_DIR, "timetable.json"),
}

# Persistence Utilities
def save_data(path, data):
    with open(path, "w") as f:
        json.dump(data, f, default=str)

def load_data(path, default):
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception:
            return default
    return default

# Initialize / Load Data into session_state
if "timetable_entries" not in st.session_state:
    st.session_state.timetable_entries = load_data(FILES["timetable"], [])

# Timetable Page Function
def timetable_page():
    st.title("📅 Timetable & Assignments")
    st.markdown("Add classes, color-code them, and track assignments.")

    # Add class form
    with st.form("add_class_form"):
        col1, col2 = st.columns(2)
        with col1:
            day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
            time = st.time_input("Class Time")
            color = st.color_picker("Class Color", value="#b3e5fc")
        with col2:
            course = st.text_input("Course Name")
            lecturer = st.text_input("Lecturer")
            notes = st.text_area("Notes / Location")
        reminder = st.checkbox("Set Reminder (simulated)")
        submit = st.form_submit_button("➕ Add Class")
        if submit and course:
            st.session_state.timetable_entries.append({
                "id": str(uuid.uuid4()),
                "day": day,
                "time": time.strftime("%I:%M %p"),
                "course": course,
                "lecturer": lecturer,
                "notes": notes,
                "color": color,
                "reminder": reminder
            })
            save_data(FILES["timetable"], st.session_state.timetable_entries)
            st.success(f"{course} added!")

    # Display timetable grouped by day
    st.subheader("Weekly Timetable")
    if st.session_state.timetable_entries:
        by_day = {}
        for t in st.session_state.timetable_entries:
            by_day.setdefault(t["day"], []).append(t)
        for d in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
            entries = by_day.get(d, [])
            if entries:
                st.markdown(f"#### {d}")
                for e in sorted(entries, key=lambda x: x["time"]):
                    st.markdown(f"""
                        <div class="card" style="margin-bottom:8px; background:{e['color']}">
                        <strong>{e['time']} - {e['course']}</strong><br>
                        👩‍🏫 {e['lecturer']}<br>
                        🗒️ {e['notes']}<br>
                        {'🔔 Reminder set' if e['reminder'] else ''}
                        </div>
                    """, unsafe_allow_html=True)
    else:
        st.info("No classes yet — add one above!")

    # Assignments
    st.markdown("---")
    st.subheader("📚 Class Assignments")
    class_choices = [e["course"] for e in st.session_state.timetable_entries] or ["General"]
    with st.form("assignment_form"):
        selected_course = st.selectbox("Select Course", class_choices)
        title = st.text_input("Assignment Title")
        status = st.selectbox("Status", ["Not Started", "In Progress", "Done"])
        due_date = st.date_input("Due Date", value=datetime.date.today())
        notes = st.text_area("Notes")
        add = st.form_submit_button("➕ Log Assignment")
        if add and title:
            st.session_state.assignments.append({
                "id": str(uuid.uuid4()),
                "course": selected_course,
                "title": title,
                "status": status,
                "due_date": due_date.isoformat(),
                "notes": notes
            })
            save_data(FILES["assignments"], st.session_state.assignments)
            st.success(f"Assignment '{title}' added for {selected_course}!")

    # Assignment filters
    st.subheader("Your Assignments")
    status_filter = st.selectbox("Filter by Status", ["All", "Not Started", "In Progress", "Done"])
    upcoming_only = st.checkbox("Show only due in next 7 days")
    today = datetime.date.today()
    filtered = []
    for a in st.session_state.assignments:
        d = datetime.date.fromisoformat(a["due_date"])
        status_ok = (status_filter == "All") or (a["status"] == status_filter)
        date_ok = (not upcoming_only) or (0 <= (d - today).days <= 7)
        if status_ok and date_ok:
            filtered.append((a, d))
    if filtered:
        for a, due in filtered:
            overdue = (due < today and a["status"] != "Done")
            bg = "#ffdddd" if overdue else "#ffffff"
            st.markdown(f"""
                <div class="card" style="margin-bottom:8px; background:{bg}">
                <strong>📝 {a['title']}</strong> — {a['course']}<br>
                📅 Due: {a['due_date']} — <em>{a['status']}</em><br>
                📌 {a['notes']}<br>
                {'<span style="color:red">🚨 Overdue!</span>' if overdue else ''}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No assignments match the filters.")

timetable_page()