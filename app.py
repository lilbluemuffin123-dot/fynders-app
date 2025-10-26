import streamlit as st
import pandas as pd
import os

# ------------------------
# APP CONFIG
# ------------------------
st.set_page_config(
    page_title="FYNDERS",
    page_icon="🧡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------
# CUSTOM CSS
# ------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
body, .stApp, .block-container, .main {
    background: linear-gradient(135deg, #ff9f43, #ff6b00);
    color: white;
    font-family: 'Helvetica', sans-serif;
}
a {color: white !important; text-decoration: none;}
p, h1, h2, h3, h4, h5, h6, li, span {color: white !important;}
.stButton>button {
    background: linear-gradient(90deg, #ffb84d, #ff6b00);
    color: white;
    font-weight: bold;
    border-radius: 15px;
    padding: 15px;
    font-size: 18px;
    width: 100%;
    transition: all 0.2s ease-in-out;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
.stDataFrame, .stMarkdown {
    border-radius: 15px;
    background: rgba(255, 255, 255, 0.08);
    padding: 15px;
    margin-bottom: 20px;
}
.card {
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    padding: 15px;
    margin-bottom: 20px;
}
.css-1d391kg {background: linear-gradient(135deg, #ffb84d, #ff6b00); color: white;}
.stTextInput>div>div>input {color: black;}
</style>
""", unsafe_allow_html=True)

# ------------------------
# SESSION STATE
# ------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

# ------------------------
# HEADER & NAV BUTTONS
# ------------------------
st.title("✨ FYNDERS — Field Outreach App")
st.subheader("Connecting Christians Worldwide")
st.markdown("Select a section below to get started:")

col1, col2 = st.columns(2)
with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("✍️ Field Entry"):
        st.session_state.page = "Field Entry"
    if st.button("🎥 Media & Resources"):
        st.session_state.page = "Media & Resources"
    if st.button("📍 Locations"):
        st.session_state.page = "Locations"
    if st.button("📜 Word of Week"):
        st.session_state.page = "Word of Week"

with col2:
    if st.button("🚨 Report an Incident"):
        st.session_state.page = "Report Incident"
    if st.button("📖 Christian Feed"):
        st.session_state.page = "Christian Feed"
    if st.button("🏛 Tabernacle of David"):
        st.session_state.page = "Tabernacle of David"
    if st.button("📋 Admin Dashboard"):
        st.session_state.page = "Admin"

# ------------------------
# PAGE SWITCHING
# ------------------------
page = st.session_state.page

# --------- HOME ----------
if page == "Home":
    st.header("🌍 Connecting Christians Worldwide")
    st.markdown("""
    **Features at your fingertips:**  
    - Give online securely; access church ministry resources.  
    - Watch videos and pictures of worship, events, and community outreach.  
    - Speak psalms, hymns, and spiritual songs and upload your own songs.  
    - Read the Bible and download e-books from the commission.  
    - Listen to 24-hour worship music and download TOD Daily prayers.  
    - Find a C25 or CC3 location near you.  
    - Report incidents affecting any member that needs urgent attention.  
    - Connect globally — translations to 7000+ languages.  
    """)
    st.markdown("**Daily Bible Verse:**")
    st.info("“For I know the plans I have for you,” declares the Lord — Jeremiah 29:11", icon="📖")

# --------- FIELD ENTRY ----------
elif page == "Field Entry":
    st.header("✍️ Field Entry")
    with st.form("field_form"):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name")
            contact_info = st.text_input("Contact Info (Phone/Email)")
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
            import datetime
            entry = {
                "Full Name": full_name,
                "Contact Info": contact_info,
                "Location": location,
                "Needs": ", ".join(needs),
                "Notes": notes,
                "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            file_path = "field_entries.csv"
            df_new = pd.DataFrame([entry])
            if os.path.exists(file_path):
                df_new.to_csv(file_path, mode='a', index=False, header=False)
            else:
                df_new.to_csv(file_path, index=False)
            st.success("✅ Entry submitted successfully!")

# --------- MEDIA ----------
elif page == "Media & Resources":
    st.header("🎥 Media & Resources")
    st.video("https://www.youtube.com/watch?v=F0OzffuqASQ")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.button("Upload Your Song / Resource")
    st.markdown("Downloadable e-books, daily prayers, and Bible study materials coming soon!")

# --------- LOCATIONS ----------
elif page == "Locations":
    st.header("📍 Find a C25 or CC3 Location")
    st.text_input("Enter City / Area")
    st.button("Search Locations")
    st.info("Locations will appear here in future versions.")

# --------- REPORT INCIDENT ----------
elif page == "Report Incident":
    st.header("🚨 Report an Incident")
    st.text_area("Describe the Incident", height=150)
    st.button("Submit Report 🧡")
    st.info("All reports are monitored by Admins.")

# --------- CHRISTIAN FEED ----------
elif page == "Christian Feed":
    st.header("📖 Christian Feed")
    posts = [
        {"verse": "Psalm 23:1-2", "text": "The Lord is my shepherd; I shall not want."},
        {"verse": "John 3:16", "text": "For God so loved the world that He gave His only Son."},
        {"verse": "Philippians 4:13", "text": "I can do all things through Christ who strengthens me."},
        {"verse": "Romans 12:12", "text": "Be joyful in hope, patient in affliction, faithful in prayer."},
        {"verse": "1 Corinthians 13:4-5", "text": "Love is patient, love is kind..."}
    ]
    for post in posts:
        st.markdown(f"<div class='card'><h3>{post['verse']}</h3><p>{post['text']}</p></div>", unsafe_allow_html=True)

# --------- WORD OF WEEK (ADMIN ONLY) ----------
elif page == "Word of Week":
    st.header("📜 Word of the Week")
    email = st.text_input("Enter your admin email to upload Word of the Week")
    if email and email.endswith("@c25.com"):
        st.session_state.is_admin = True
    elif email and not email.endswith("@c25.com"):
        st.warning("❌ Invalid email. Must end with @c25.com")

    if st.session_state.is_admin:
        uploaded_file = st.file_uploader("Upload Lecture (PDF/Text/Image)", type=["pdf", "txt", "jpg", "png"])
        if uploaded_file:
            uploads_dir = "word_of_week_uploads"
            os.makedirs(uploads_dir, exist_ok=True)
            file_path = os.path.join(uploads_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"✅ Uploaded successfully: {uploaded_file.name}")

        if os.path.exists("word_of_week_uploads"):
            st.subheader("📚 Available Lectures")
            for f in os.listdir("word_of_week_uploads"):
                st.markdown(f"- {f}")
    else:
        st.info("🔒 Admin access required to upload or view Word of the Week.")

# --------- TABERNACLE OF DAVID (ADMIN ONLY) ----------
elif page == "Tabernacle of David":
    st.header("🏛 Tabernacle of David")
    email = st.text_input("Enter your admin email to upload materials")
    if email and email.endswith("@c25.com"):
        st.session_state.is_admin = True
    elif email and not email.endswith("@c25.com"):
        st.warning("❌ Invalid email. Must end with @c25.com")

    if st.session_state.is_admin:
        pdf_file = st.file_uploader("Upload PDF (Devotional/Worship Material)", type=["pdf"])
        if pdf_file:
            tod_dir = "tabernacle_of_david"
            os.makedirs(tod_dir, exist_ok=True)
            file_path = os.path.join(tod_dir, pdf_file.name)
            with open(file_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            st.success(f"✅ PDF uploaded successfully: {pdf_file.name}")

        if os.path.exists("tabernacle_of_david"):
            st.subheader("📂 Available Tabernacle Files")
            for pdf in os.listdir("tabernacle_of_david"):
                st.markdown(f"- {pdf}")
    else:
        st.info("🔒 Admin access required to upload or view Tabernacle of David materials.")

# --------- ADMIN DASHBOARD ----------
elif page == "Admin":
    st.header("📋 Admin Dashboard")
    email = st.text_input("Enter your admin email")
    if email:
        if email.endswith("@c25.com"):
            st.session_state.is_admin = True
            st.header("📋 Admin Dashboard – Follow-Up Overview")
            file_path = "field_entries.csv"
            if os.path.exists(file_path):
                entries_df = pd.read_csv(file_path)
                if entries_df.empty:
                    st.info("No field entries submitted yet.")
                else:
                    st.dataframe(entries_df, use_container_width=True)
            else:
                st.info("No field entries submitted yet.")
        else:
            st.warning("❌ Invalid email. Please enter a valid @c25.com email.")
