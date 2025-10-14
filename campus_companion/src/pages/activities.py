import streamlit as st
import uuid
import json
import os
import datetime
from utils.persistence import save_data, load_data
from config import FILES

# ----------------------------
# 🌟 Activities Page
# ----------------------------

def activities_page():
    st.title("🎉 Campus Activities")
    st.write("Create public events and personal schedule items.")

    st.subheader("Create an Event for Everyone")
    with st.form("public_event_form"):
        ev_title = st.text_input("Event Title")
        ev_date = st.date_input("Event Date", value=datetime.date.today())
        ev_time = st.time_input("Event Time")
        ev_loc = st.text_input("Location")
        ev_type = st.selectbox("Event Type", ["Social", "Academic", "Club", "Other"])
        ev_color = st.color_picker("Event Color", value="#cfe9ff")
        ev_pick = st.checkbox("Mark as User's Pick (spotlight)")
        ev_desc = st.text_area("Description")
        add_ev = st.form_submit_button("✅ Add Event")
        if add_ev and ev_title:
            event = {
                "id": str(uuid.uuid4()),
                "title": ev_title,
                "date": ev_date.isoformat(),
                "time": ev_time.strftime("%I:%M %p"),
                "location": ev_loc,
                "type": ev_type,
                "color": ev_color,
                "user_pick": ev_pick,
                "description": ev_desc or "No description"
            }
            st.session_state.all_events.append(event)
            save_data(FILES["events"], st.session_state.all_events)
            st.success("🎉 Event added!")

    st.markdown("---")
    st.subheader("Upcoming Campus Events")
    today = datetime.date.today()
    if st.session_state.all_events:
        for e in sorted(st.session_state.all_events, key=lambda x: x["date"]):
            days_left = (datetime.date.fromisoformat(e["date"]) - today).days
            st.markdown(f"""
                <div class="card" style="margin-bottom:10px; background:{e['color']}">
                <strong>🎫 {e['title']}</strong> — {e['type']}<br>
                📍 {e['location']} | 🕒 {e['time']} | 📅 {e['date']}<br>
                📝 {e['description']}<br>
                {'⏳ Starts in ' + str(days_left) + ' day(s)' if days_left >= 0 else '🚨 Happened already'}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No campus events yet — add one above!")

    st.markdown("---")
    st.subheader("Your Personal Schedule")
    username = st.text_input("Your name (for personal schedule)", value="Daniella")
    if "personal_schedules" not in st.session_state:
        st.session_state.personal_schedules = {}

    if username and username not in st.session_state.personal_schedules:
        st.session_state.personal_schedules[username] = []

    with st.form("personal_event_form"):
        ptitle = st.text_input("Task Title")
        pdate = st.date_input("Task Date", value=today)
        ptime = st.time_input("Task Time")
        pdesc = st.text_area("Notes")
        pcolor = st.color_picker("Color tag", value="#e3f2fd")
        psave = st.form_submit_button("➕ Add Personal Task")
        if psave and ptitle:
            st.session_state.personal_schedules.setdefault(username, []).append({
                "id": str(uuid.uuid4()),
                "title": ptitle,
                "date": pdate.isoformat(),
                "time": ptime.strftime("%I:%M %p"),
                "description": pdesc,
                "color": pcolor
            })
            st.success(f"Added personal task '{ptitle}'")

    st.markdown(f"#### Tasks for {username} (today)")
    tasks = st.session_state.personal_schedules.get(username, [])
    for t in tasks:
        if datetime.date.fromisoformat(t["date"]) == today:
            st.markdown(f"""
                <div class="card" style="margin-bottom:8px; background:{t['color']}">
                📌 <strong>{t['title']}</strong><br>
                🕒 {t['time']}<br>
                📝 {t['description']}
                </div>
            """, unsafe_allow_html=True)