import streamlit as st
import pandas as pd

# ------------------------
# APP CONFIG
# ------------------------
st.set_page_config(page_title="FYNDERS", page_icon="🧡", layout="wide")

# ------------------------
# CUSTOM CSS FOR ORANGE THEME
# ------------------------
st.markdown("""
<style>
/* General page */
body {
    background-color: #fff7f0;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: #e37222;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #ff9f43, #ff6b00);
    color: white;
    font-weight: bold;
}

/* Sidebar */
.css-1d391kg {background-color: #ffe6cc;}
</style>
""", unsafe_allow_html=True)

# ------------------------
# HEADER
# ------------------------
st.title("✨ FYNDERS — Field Outreach App")
st.caption("A mock UI demo (no backend logic)")

# ------------------------
# SIDEBAR: SELECT SECTION
# ------------------------
section = st.sidebar.radio("Select Section", ["Newcomer", "Admin"])

# ------------------------
# NEWCOMER SECTION
# ------------------------
if section == "Newcomer":
    st.header("Welcome to FYNDERS — Newcomer Section")
    
    submenu = st.sidebar.selectbox("Menu", ["Home", "Field Entry", "Media & Resources", "Locations", "Report an Incident"])
    
    # --------- HOME ----------
    if submenu == "Home":
        st.header("🌍 Connecting Christians Worldwide")
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            **Features at your fingertips:**  
            - Give online through our secure portal; books and church ministry resources available.  
            - Watch videos and pictures of events worldwide, meet friends, share testimonies.  
            - Speak psalms, hymns, spiritual songs and upload your own songs.  
            - Read the Bible and download E-books from the commission.  
            - Listen to 24-hour music ministrations and download TOD Daily prayers.  
            - Seek and find a C25 or CC3 location near you.  
            - Quickly report any incidents needing urgent attention.  
            - Connect globally — features to translate to 7000+ languages.  
            - Social features similar to Facebook & Instagram for Christians.
            """)
            st.markdown("**Daily Bible Verse:**")
            st.info("“For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future.” — Jeremiah 29:11")
        with col2:
            st.image("https://images.unsplash.com/photo-1603133872877-96c4a4f64ebd?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTR8fGJpYmxlfGVufDB8fDB8fA%3D%3D&ixlib=rb-4.0.3&q=80&w=400", 
                     caption="Community Outreach", use_container_width=True)
        st.markdown("---")
    
    # --------- FIELD ENTRY ----------
    elif submenu == "Field Entry":
        st.header("✍️ Field Data Entry")
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
    elif submenu == "Media & Resources":
        st.header("🎥 Media & Resources")
        col1, col2 = st.columns([2,1])
        with col1:
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
            st.button("Upload Your Song / Resource")
            st.markdown("Downloadable e-books, daily prayers, and Bible study materials coming soon!")
            st.markdown("**Featured Bible Images:**")
            st.image("https://images.unsplash.com/photo-1596690934914-210c8ef9f67e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8Y2hyaXN0aWFuJTIwYmlibGV8ZW58MHwwfDB8fA%3D%3D&ixlib=rb-4.0.3&q=80&w=400", use_container_width=True)
        with col2:
            st.image("https://images.unsplash.com/photo-1586880244406-6d9d2b5d26c0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8Y2hyaXN0aWFuJTIwbWluaXN0cnl8ZW58MHwwfDB8fA%3D%3D&ixlib=rb-4.0.3&q=80&w=300", caption="Community Media", use_container_width=True)
    
    # --------- LOCATIONS ----------
    elif submenu == "Locations":
        st.header("📍 Find a C25 or CC3 Location")
        st.text_input("Enter City / Area")
        st.button("Search Locations")
        st.info("Locations will appear here in future versions.")
    
    # --------- REPORT INCIDENT ----------
    elif submenu == "Report an Incident":
        st.header("🚨 Report an Incident")
        st.text_area("Describe the Incident", height=150)
        st.button("Submit Report 🧡")
        st.info("All reports are monitored by Admins.")

# ------------------------
# ADMIN SECTION (EMAIL LOGIN)
# ------------------------
elif section == "Admin":
    st.header("📋 Admin Section")
    
    email = st.text_input("Enter your admin email (must be @c25.com)")
    
    if email.endswith("@c25.com") and email != "":
        submenu = st.sidebar.selectbox("Menu", ["Dashboard"])
        
        if submenu == "Dashboard":
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
