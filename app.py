import streamlit as st
import pandas as pd
import random

# ------------------------
# APP CONFIG
# ------------------------
st.set_page_config(page_title="FYNDERS", page_icon="🧡", layout="wide")
st.title("✨ FYNDERS — Field Outreach App")
st.write("🚀 App is starting...")  # debug message to ensure app loads

# ------------------------
# MOCK DATABASE (in-memory)
# ------------------------
if "users" not in st.session_state:
    st.session_state["users"] = {}  # key=email, value=role

if "field_logs" not in st.session_state:
    st.session_state["field_logs"] = []  # list of dicts for entries

# ------------------------
# LOGIN PAGE
# ------------------------
if "email" not in st.session_state:
    st.write("Please log in with your C25 email to access the system.")
    email_input = st.text_input("Email (@c25.com)")
    if st.button("Login"):
        if email_input.endswith("@c25.com"):
            st.session_state["users"].setdefault(email_input, "Field Worker")
            st.session_state["email"] = email_input
            st.success(f"Logged in as **{email_input}**")
        else:
            st.error("Please use a valid @c25.com email address.")

# ------------------------
# MAIN APP
# ------------------------
if "email" in st.session_state:
    email = st.session_state["email"]
    st.sidebar.success(f"Welcome {email} 👋")
    menu = st.sidebar.selectbox("Menu", ["Home", "Field Entry", "Admin Dashboard"])

    # ---------- HOME ----------
    if menu == "Home":
        st.header("Welcome to FYNDERS")
        st.write("A platform to connect Christians who want to make a difference — together.")

    # ---------- FIELD ENTRY ----------
    elif menu == "Field Entry":
        st.header("✍️ Field Data Entry")
        with st.form("field_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Full Name")
                contact = st.text_input("Contact Info (Phone/Email)")
                location = st.text_input("Location (City / Area)")
            with col2:
                needs = st.multiselect(
                    "Needs / Requests",
                    ["Follow-Up", "Welfare – Food", "Counselling", "Prayer", "Bible Materials", "Visit"],
                    default=["Follow-Up"]
                )
                notes = st.text_area("Notes / Additional Details", height=120)
            submitted = st.form_submit_button("Submit Entry 🧡")
            if submitted:
                if name and contact and location:
                    FOLLOWUP_TEAM = ["John Doe", "Mary Faith", "Samuel Hope", "Esther Joy", "Grace Light"]
                    assigned_to = random.choice(FOLLOWUP_TEAM)
                    date = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
                    entry = {
                        "name": name,
                        "contact": contact,
                        "location": location,
                        "needs": ", ".join(needs),
                        "notes": notes,
                        "date": date,
                        "assigned_to": assigned_to,
                        "status": "Assigned"
                    }
                    st.session_state["field_logs"].append(entry)
                    st.success(f"Entry for **{name}** logged successfully. Assigned to **{assigned_to}**.")
                else:
                    st.warning("Please fill in all required fields.")

    # ---------- ADMIN DASHBOARD ----------
    elif menu == "Admin Dashboard":
        st.header("📋 Admin Dashboard – Follow-Up Overview")
        if st.session_state["field_logs"]:
            df = pd.DataFrame(st.session_state["field_logs"])
            st.dataframe(df)
        else:
            st.info("No records yet. Field workers can start logging entries from the Field Entry page.")
