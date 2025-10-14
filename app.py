import streamlit as st
import pandas as pd

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
/* Hide Streamlit default menu, footer, header */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Full page background */
body, .stApp, .block-container, .main {
    background: linear-gradient(135deg, #ff9f43, #ff6b00);
    color: white;
    font-family: 'Helvetica', sans-serif;
}

/* All text white */
a {color: white !important; text-decoration: none;}
p, h1, h2, h3, h4, h5, h6, li, span {color: white !important;}

/* Buttons */
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

/* Feed posts and tables styling */
.stDataFrame, .stMarkdown {
    border-radius: 15px;
    background: rgba(255, 255, 255, 0.08);
    padding: 15px;
    margin-bottom: 20px;
}

/* Cards for feed posts */
.card {
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    padding: 15px;
    margin-bottom: 20px;
}

/* Sidebar styling */
.css-1d391kg {background: linear-gradient(135deg, #ffb84d, #ff6b00); color: white;}
.stTextInput>div>div>input {
    color: black;
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# HOME PAGE
# ------------------------
st.title("✨ FYNDERS — Field Outreach App")
st.subheader("Connecting Christians Worldwide")
st.markdown("Select a section below to get started:")

# Session state to track current page
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Main buttons
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

with col2:
    if st.button("🚨 Report an Incident"):
        st.session_state.page = "Report Incident"
    if st.button("📖 Christian Feed"):
        st.session_state.page = "Christian Feed"
    if st.button("📋 Admin Dashboard"):
        st.session_state.page = "Admin"

# ------------------------
# PAGES
# ------------------------
page = st.session_state.page

# --------- HOME PAGE ----------
if page == "Home":
    st.header("🌍 Connecting Christians Worldwide")
    st.markdown("""
    **Features at your fingertips:**  
    - Give online securely; access church ministry resources.  
    - Watch videos and pictures of worship, events, and community outreach.  
    - Speak psalms, hymns, spiritual songs and upload your own songs.  
    - Read the Bible and download e-books from the commission.  
    - Listen to 24-hour worship music and download TOD Daily prayers.  
    - Find a C25 or CC3 location near you.  
    - Report incidents affecting any member that needs urgent attention.  
    - Connect globally — translations to 7000+ languages.  
    """)
    st.markdown("**Daily Bible Verse:**")
    st.info("“For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future.” — Jeremiah 29:11", icon="📖")

# --------- FIELD ENTRY ----------
elif page == "Requests":
    st.header("✍️ Requests")
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

# --------- MEDIA & RESOURCES ----------
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
    st.markdown("A feed of Bible verses and inspirational posts from the community.")
    posts = [
        {"verse": "Psalm 23:1-2", "text": "The Lord is my shepherd; I shall not want."},
        {"verse": "John 3:16", "text": "For God so loved the world that He gave His only Son."},
        {"verse": "Philippians 4:13", "text": "I can do all things through Christ who strengthens me."},
        {"verse": "Romans 12:12", "text": "Be joyful in hope, patient in affliction, faithful in prayer."},
        {"verse": "1 Corinthians 13:4-5", "text": "Love is patient, love is kind..."}
    ]
    for post in posts:
        st.markdown(f"<div class='card'><h3>{post['verse']}</h3><p>{post['text']}</p></div>", unsafe_allow_html=True)

# --------- ADMIN DASHBOARD ----------
elif page == "Admin":
    st.header("📋 Admin Dashboard")
    email = st.text_input("Enter your admin email")
    
    if email.endswith("@c25.com") and email != "":
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
    elif email != "":
        st.warning("❌ Invalid email. Please enter a valid @c25.com email.")


