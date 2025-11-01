import streamlit as st
import pandas as pd
import os
import base64
import datetime
import time

# ------------------------
# CONFIG
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
body, .stApp, .block-container, .main {background: linear-gradient(135deg, #ff9f43, #ff6b00); color: white; font-family: 'Helvetica', sans-serif;}
a {color: white !important; text-decoration: none;}
p, h1, h2, h3, h4, h5, h6, li, span {color: white !important;}
.stButton>button {background: linear-gradient(90deg, #ffb84d, #ff6b00); color: white; font-weight: bold; border-radius: 15px; padding: 15px; font-size: 18px; width: 100%; transition: all 0.2s ease-in-out;}
.stButton>button:hover {transform: scale(1.05); box-shadow: 0 4px 15px rgba(0,0,0,0.3);}
.stDataFrame, .stMarkdown {border-radius: 15px; background: rgba(255, 255, 255, 0.08); padding: 15px; margin-bottom: 20px;}
.card {border-radius: 15px; background: rgba(255,255,255,0.05); padding: 15px; margin-bottom: 20px;}
.css-1d391kg {background: linear-gradient(135deg, #ffb84d, #ff6b00); color: white;}
.stTextInput>div>div>input {color: white;}
.stTextArea textarea {color: white;}

/* MOBILE VIEW INPUT STYLING */
@media (max-width: 768px) {
    .stTextInput>div>div>input, .stTextArea textarea {
        background-color: black !important;
        color: white !important;
    }
}

/* CHAT BUBBLES */
.chat-bubble {
    max-width: 80%;
    padding: 10px 15px;
    margin: 5px;
    border-radius: 15px;
    display: inline-block;
    clear: both;
    word-wrap: break-word;
}
.chat-bubble.admin {
    background-color: #34b7f1;
    color: white;
    float: right;
}
.chat-bubble.user {
    background-color: #ece5dd;
    color: black;
    float: left;
}
.chat-timestamp {
    font-size: 10px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# UPLOAD FOLDER & CSV
# ------------------------
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
DB_FILE = "uploads_db.csv"

if os.path.exists(DB_FILE):
    db = pd.read_csv(DB_FILE)
    if not db.empty:
        db['timestamp'] = pd.to_datetime(db['timestamp'], errors='coerce')
else:
    db = pd.DataFrame(columns=["type","file_path","text","timestamp"])

# ------------------------
# SESSION STATE
# ------------------------
if "page" not in st.session_state: st.session_state.page = "Home"
if "is_admin" not in st.session_state: st.session_state.is_admin = False
if "chat_refresh" not in st.session_state: st.session_state.chat_refresh = time.time()

# ------------------------
# LOGIN
# ------------------------
st.sidebar.header("Login")
email = st.sidebar.text_input("Enter your email")
is_admin = email.lower().endswith("@c25.com") if email else False
st.session_state.is_admin = is_admin

if email:
    if is_admin: st.sidebar.success(f"✅ Logged in as Admin: {email}")
    else: st.sidebar.info(f"👤 Logged in as Public User: {email}")
else:
    st.sidebar.warning("Please enter your email to continue.")

# ------------------------
# NAVIGATION
# ------------------------
st.title("✨ FYNDERS — Field Outreach App")
st.subheader("Connecting Christians Worldwide")
st.markdown("Select a section below to get started:")

col1, col2 = st.columns(2)
with col1:
    if st.button("🏠 Home"): st.session_state.page = "Home"
    if st.button("✍️ Field Entry"): st.session_state.page = "Field Entry"
    if st.button("🎥 Media & Resources"): st.session_state.page = "Media & Resources"
    if st.button("📍 Locations"): st.session_state.page = "Locations"
    if st.button("📜 Word of Week"): st.session_state.page = "Word of Week"
with col2:
    if st.button("🚨 Report an Incident"): st.session_state.page = "Report Incident"
    if st.button("📖 Christian Feed"): st.session_state.page = "Christian Feed"
    if st.button("🏛 Tabernacle of David"): st.session_state.page = "Tabernacle of David"
    if st.button("💬 Internal Chat"): st.session_state.page = "Internal Chat"
    if st.button("💳 Donations / Giving"): st.session_state.page = "Donations"
    if st.button("ℹ️ About Us"): st.session_state.page = "About Us"
    if st.button("🛠 Services"): st.session_state.page = "Services"
    if st.button("🛒 Store"): st.session_state.page = "Store"
    if st.button("📋 Admin Dashboard"): st.session_state.page = "Admin"

page = st.session_state.page

# ------------------------
# DOWNLOAD HELPER
# ------------------------
def get_download_link(file_path, label):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{os.path.basename(file_path)}" style="color:#ffcc70;">📥 {label}</a>'

# ------------------------
# AUTO-REFRESH CHAT FUNCTION
# ------------------------
def auto_refresh_chat(interval_sec=3):
    if time.time() - st.session_state.chat_refresh > interval_sec:
        st.session_state.chat_refresh = time.time()
        st.experimental_rerun()

# ------------------------
# HOME PAGE
# ------------------------
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
    st.info("“For I know the plans I have for you,” declares the Lord — Jeremiah 29:11", icon="📖")

# ------------------------
# FIELD ENTRY
# ------------------------
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
            entry = {
                "Full Name": full_name,
                "Contact Info": contact_info,
                "Location": location,
                "Needs": ", ".join(needs),
                "Notes": notes,
                "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            file_path = "field_entries.csv"
            backup_path = "field_entries_backup.csv"
            df_new = pd.DataFrame([entry])

            # Save main CSV
            if os.path.exists(file_path):
                df_new.to_csv(file_path, mode='a', index=False, header=False)
            else:
                df_new.to_csv(file_path, index=False)

            # Always update backup CSV
            if os.path.exists(backup_path):
                df_new.to_csv(backup_path, mode='a', index=False, header=False)
            else:
                df_new.to_csv(backup_path, index=False)

            st.success("✅ Entry submitted successfully and saved securely!")

# ------------------------
# MEDIA & RESOURCES
# ------------------------
elif page == "Media & Resources":
    st.header("🎥 Media & Resources")
    st.video("https://www.youtube.com/watch?v=F0OzffuqASQ")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.button("Upload Your Song / Resource")
    st.markdown("Downloadable e-books, daily prayers, and Bible study materials coming soon!")

# ------------------------
# LOCATIONS
# ------------------------
elif page == "Locations":
    st.header("📍 Find a C25 or CC3 Location")
    office_address = "135 W 56th Street, New York, New York 10019, 9TH Floor"
    latitude = 40.7651
    longitude = -73.9819
    user_input = st.text_input("Enter City / Area")
    if st.button("Search Locations"):
        st.success(f"📍 Our Office Location:\n{office_address}")
        st.map(pd.DataFrame([[latitude, longitude]], columns=["lat", "lon"]))

# ------------------------
# REPORT INCIDENT
# ------------------------
elif page == "Report Incident":
    st.header("🚨 Report an Incident")
    st.text_area("Describe the Incident", height=150)
    st.button("Submit Report 🧡")
    st.info("All reports are monitored by Admins.")

# ------------------------
# CHRISTIAN FEED
# ------------------------
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

# ------------------------
# WORD OF THE WEEK
# ------------------------
elif page == "Word of Week":
    st.header("📖 Word of the Week")
    word_files = db[db['type'] == "word_of_week"]
    latest_file_path = None
    if not word_files.empty:
        latest = word_files.sort_values("timestamp").iloc[-1]
        latest_file_path = latest['file_path']
        file_ext = os.path.splitext(latest_file_path)[1].lower()
        if file_ext == ".pdf":
            st.markdown(get_download_link(latest_file_path, "Download PDF"), unsafe_allow_html=True)
        elif file_ext in [".png", ".jpg", ".jpeg"]:
            st.image(latest_file_path, caption="Word of the Week Image", use_container_width=True)
            st.markdown(get_download_link(latest_file_path, "Download Image"), unsafe_allow_html=True)
        else:
            with open(latest_file_path, "r", encoding="utf-8") as f: st.text(f.read())
            st.markdown(get_download_link(latest_file_path, "Download Text File"), unsafe_allow_html=True)
    else:
        st.info("No Word of the Week uploaded yet.")

    if is_admin:
        upload = st.file_uploader(
            "Upload Word of the Week (PDF/Image/Text)", 
            type=["pdf","png","jpg","jpeg","txt"],
            key="word_upload",
            help="Current: " + (os.path.basename(latest_file_path) if latest_file_path else "None")
        )
        if upload:
            save_path = os.path.join(UPLOAD_DIR, upload.name)
            with open(save_path, "wb") as f: f.write(upload.read())
            new_row = {"type":"word_of_week","file_path":save_path,"text":"","timestamp":datetime.datetime.now()}
            db = pd.concat([db, pd.DataFrame([new_row])], ignore_index=True)
            db.to_csv(DB_FILE,index=False)
            st.success("✅ Word of the Week uploaded successfully!")

# ------------------------
# TABERNACLE
# ------------------------
elif page == "Tabernacle of David":
    st.header("🏛 Tabernacle of David")
    tab_files = db[db['type'] == "tabernacle"]
    latest_file_path = None
    if not tab_files.empty:
        latest = tab_files.sort_values("timestamp").iloc[-1]
        latest_file_path = latest['file_path']
        st.markdown(get_download_link(latest_file_path, "Download Tabernacle PDF"), unsafe_allow_html=True)
    else:
        st.info("No Tabernacle uploaded yet.")

    if is_admin:
        upload = st.file_uploader(
            "Upload Tabernacle PDF", 
            type=["pdf"],
            key="tab_upload",
            help="Current: " + (os.path.basename(latest_file_path) if latest_file_path else "None")
        )
        if upload:
            save_path = os.path.join(UPLOAD_DIR, upload.name)
            with open(save_path, "wb") as f: f.write(upload.read())
            new_row = {"type":"tabernacle","file_path":save_path,"text":"","timestamp":datetime.datetime.now()}
            db = pd.concat([db, pd.DataFrame([new_row])], ignore_index=True)
            db.to_csv(DB_FILE,index=False)
            st.success("✅ Tabernacle uploaded successfully!")

# ------------------------
# INTERNAL LIVE CHAT
# ------------------------
# ------------------------
# INTERNAL LIVE CHAT
# ------------------------
elif page == "Internal Chat":
    st.header("💬 Internal Admin Chat")
    if not is_admin:
        st.warning("❌ Only admin emails can access this chat.")
        st.stop()

    CHAT_FILE = "live_chat.csv"
    if not os.path.exists(CHAT_FILE):
        pd.DataFrame(columns=["timestamp","user","message"]).to_csv(CHAT_FILE, index=False)

    # --- Load chat ---
    chat_df = pd.read_csv(CHAT_FILE)
    
    # Scroll chat to show latest messages
    st.markdown("<div style='max-height:400px; overflow-y:scroll;'>", unsafe_allow_html=True)
    if not chat_df.empty:
        for _, row in chat_df.iterrows():
            bubble_class = "admin" if row['user'].endswith("@c25.com") else "user"
            st.markdown(f"""
            <div class='chat-bubble {bubble_class}'>
                <strong>{row['user']}</strong>: {row['message']}
                <div class='chat-timestamp'>{row['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Send new message ---
    with st.form("chat_form"):
        message = st.text_input("Type your message here...")
        send = st.form_submit_button("Send")
        if send and message:
            new_message = pd.DataFrame([{
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "user": email,
                "message": message
            }])
            new_message.to_csv(CHAT_FILE, mode="a", index=False, header=False)
            st.experimental_rerun()  # rerun only after sending

    # --- Auto-refresh without rerunning while typing ---
    st_autorefresh = st.empty()
    if time.time() - st.session_state.get("chat_refresh", 0) > 3:
        st.session_state["chat_refresh"] = time.time()
        st_autorefresh.markdown("<meta http-equiv='refresh' content='3'>", unsafe_allow_html=True)
# ------------------------
# DONATIONS PAGE
# ------------------------
elif page == "Donations":
    st.header("💳 Donations / Giving")
    st.info("Connect your donations securely. Bank integration coming soon.")
    st.text_input("Enter Amount")
    st.button("Donate 🧡")

# ------------------------
# ABOUT US PAGE
# ------------------------
elif page == "About Us":
    st.header("ℹ️ About Us")
    st.markdown("""
    **About Apostle:**  
    [Write about the Apostle here]  

    **Mission Statement:**  
    [Write mission statement here]
    """)

# ------------------------
# SERVICES PAGE
# ------------------------
elif page == "Services":
    st.header("🛠 Our Services")
    st.markdown("""
    - Community Outreach  
    - Bible Study & Counseling  
    - Worship Events  
    - Field Ministry  
    """)

# ------------------------
# STORE PAGE
# ------------------------
elif page == "Store":
    st.header("🛒 Store")
    st.markdown("Coming soon: Buy books, resources, and merchandise here.")

# ------------------------
# ADMIN DASHBOARD
# ------------------------
elif page == "Admin":
    st.header("📋 Admin Dashboard")
    email_input = st.text_input("Enter your admin email")
    if email_input:
        if email_input.endswith("@c25.com"):
            st.session_state.is_admin = True
            st.header("📋 Admin Dashboard – Follow-Up Overview")
            file_path = "field_entries.csv"
            backup_path = "field_entries_backup.csv"

            # Read main CSV, if missing, try backup
            if os.path.exists(file_path):
                entries_df = pd.read_csv(file_path)
            elif os.path.exists(backup_path):
                entries_df = pd.read_csv(backup_path)
                st.warning("⚠️ Main CSV missing. Loaded from backup.")
            else:
                entries_df = pd.DataFrame()

            if entries_df.empty:
                st.info("No field entries submitted yet.")
            else:
                st.dataframe(entries_df, use_container_width=True)
        else:
            st.warning("❌ Invalid email. Please enter a valid @c25.com email.")
