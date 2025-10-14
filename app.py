import streamlit as st
import pandas as pd

# ------------------------
# APP CONFIG
# ------------------------
st.set_page_config(page_title="FYNDERS", page_icon="🧡", layout="wide")

# ------------------------
# HEADER
# ------------------------
st.title("✨ FYNDERS — Field Outreach App")
st.caption("A mock UI demo (no backend logic)")

# ------------------------
# SIDEBAR MENU
# ------------------------
menu = st.sidebar.selectbox("Menu", ["Home", "Field Entry", "Admin Dashboard", "Login"])

# ------------------------
# HOME
# ------------------------
if menu == "Home":
    st.header("Welcome to FYNDERS")
    st.write("A platform to connect Christians who want to make a difference — together.")
    st.image("https://placekitten.com/600/300", caption="Community Outreach")

# ------------------------
# FIELD ENTRY (UI ONLY)
# ------------------------
elif menu == "Field Entry":
    st.header("✍️ Field Data Entry")
    st.write("Fill in the details below (form is not functional in this UI-only demo).")

    with st.form("field_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name")
            st.text_input("Contact Info (Phone/Email)")
            st.text_input("Location (City / Area)")
        with col2:
            st.multiselect(
                "Needs / Requests",
                ["Follow-Up", "Welfare – Food", "Counselling", "Prayer", "Bible Materials", "Visit"],
                default=["Follow-Up"]
            )
            st.text_area("Notes / Additional Details", height=120)
        st.form_submit_button("Submit Entry 🧡")

# ------------------------
# ADMIN DASHBOARD (UI ONLY)
# ------------------------
elif menu == "Admin Dashboard":
    st.header("📋 Admin Dashboard – Follow-Up Overview")
    st.info("This is a sample data preview.")
    sample_data = pd.DataFrame({
        "Name": ["John Doe", "Mary Faith"],
        "Location": ["Toronto", "New York"],
        "Needs": ["Counselling, Prayer", "Welfare – Food"],
        "Assigned To": ["Samuel Hope", "Grace Light"],
        "Status": ["Assigned", "In Progress"],
        "Date": ["2025-10-12 09:15", "2025-10-12 10:30"]
    })
    st.dataframe(sample_data, use_container_width=True)

# ------------------------
# LOGIN PAGE (UI ONLY)
# ------------------------
elif menu == "Login":
    st.header("🔐 Login")
    st.text_input("Email (@c25.com)")
    st.button("Login")
    st.info("Login is disabled in this demo.")
