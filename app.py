import streamlit as st
import pandas as pd
import sqlite3
import streamlit_authenticator as stauth

# ------------------------
# DATABASE SETUP
# ------------------------
conn = sqlite3.connect("fynders.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT,
    role TEXT
)
""")
conn.commit()

# ------------------------
# AUTHENTICATION SETUP
# ------------------------
# You can edit usernames/passwords here or later store them in DB
names = ["Admin User", "Field Worker"]
usernames = ["admin", "worker"]
passwords = ["admin123", "worker123"]

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "fynder_cookie",
    "fynder_signature",
    cookie_expiry_days=30,
)

name, authentication_status, username = authenticator.login("Login", "main")

# ------------------------
# LOGIN LOGIC
# ------------------------
if authentication_status is False:
    st.error("Username/password is incorrect")

elif authentication_status is None:
    st.warning("Please enter your username and password")

elif authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {name} 👋")

    # ------------------------
    # MAIN APP
    # ------------------------
    st.title("✨ FYNDERS — Bringing Christians Together")

    menu = st.sidebar.selectbox("Menu", ["Home", "Finders Network", "Field Worker Dashboard"])

    if menu == "Home":
        st.header("Welcome to FYNDERS")
        st.write("A platform to connect Christians who want to make a difference — together.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/2/21/Cross-Christian-symbol.svg", width=150)

    elif menu == "Finders Network":
        st.subheader("🌍 Connect with others")
        name_input = st.text_input("Name")
        email_input = st.text_input("Email")
        role_input = st.selectbox("Role", ["Volunteer", "Field Worker", "Leader"])

        if st.button("Join Network"):
            if name_input and email_input:
                cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (name_input, email_input, role_input))
                conn.commit()
                st.success(f"{name_input} added to the FYNDERS Network!")
            else:
                st.warning("Please fill in all fields.")

        df = pd.read_sql("SELECT * FROM users", conn)
        st.dataframe(df)

    elif menu == "Field Worker Dashboard":
        st.subheader("🕊️ Field Worker Dashboard")
        st.write("Manage your missions, reports, and connections here.")
        st.info("Coming soon: map view, prayer requests, and event tracking!")
