import streamlit as st
import plotly.express as px
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Anurag's Dataverse", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM DARK THEME CSS ---
st.markdown(
    """
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        h1, h2, h3 {
            color: #00FFCC;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #00FFCC;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- BALLOON EFFECT ON LOAD ---
st.balloons()

# --- HERO SECTION ---
st.markdown("<h1 style='text-align: center;'>🌌 Welcome to Anurag's Dataverse</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Data Analyst | ML Explorer | Visualization Alchemist</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Creating impact through code, charts, and a touch of magic ✨</p>", unsafe_allow_html=True)

# --- SOCIAL LINKS ---
st.markdown("### 🔗 Connect With Me")
st.markdown(
    """
    - [Kaggle Profile](https://www.kaggle.com/anuragvenkatayogi)
    - [GitHub](https://github.com/anurag-hacker9)
    - [LinkedIn](https://www.linkedin.com/in/anuragvenkatayogi/)
    """
)

# --- INTERACTIVE SKILLSET DASHBOARD ---
st.markdown("## 🚀 Skillset Visualizer")

skills = {
    "Python": 95,
    "SQL": 90,
    "Tableau": 88,
    "Power BI": 85,
    "Machine Learning": 92,
    "Geospatial Analysis": 80,
    "CRM Tools": 75,
    "EDA & Data Prep": 94
}

skill_df = pd.DataFrame({
    "Skill": list(skills.keys()),
    "Proficiency": list(skills.values())
})

fig = px.bar(skill_df, x="Proficiency", y="Skill", orientation="h", color="Skill",
             title="Interactive Skill Proficiency Chart", color_discrete_sequence=px.colors.sequential.Turbo)
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(20,20,20,0.8)', font_color="white")
st.plotly_chart(fig, use_container_width=True)

# --- PROJECT SHOWCASE ---
st.markdown("## 🌟 Project Highlights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 AI-Powered Exam Monitoring")
    st.markdown("- YOLOv8 object detection, smart zoom, Wi-Fi/Bluetooth tracking")
    st.markdown("- Achieved 93% detection accuracy, reduced manual efforts by 70%")
    st.markdown("[View on GitHub](https://github.com/anurag-github/exam-proctoring)")

with col2:
    st.markdown("### 🏡 Airbnb Price Prediction + Chatbot")
    st.markdown("- Regression model with 78% accuracy, interactive AI chatbot")
    st.markdown("- Boosted booking efficiency and reduced host response time")
    st.markdown("[View on GitHub](https://github.com/anurag-github/airbnb-chatbot)")

# --- CAREER TIMELINE ---
st.markdown("## 📅 Career Timeline")

timeline_df = pd.DataFrame({
    "Position": ["Programmer Analyst Trainee", "Intern - DRDL", "Graduate Assistant Analyst", "MS Business Analytics"],
    "Year": ["2021", "2022", "2023", "2023–2025"]
})
st.dataframe(timeline_df)

# --- CONTACT SECTION ---
st.markdown("## 📬 Say Hello")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    message = st.text_area("Your Message")
    send = st.form_submit_button("Send Message 🎉")
    if send:
        st.success("🎈 Thanks for reaching out! I’ll get back to you soon.")

# --- FOOTER ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© 2025 Anurag Venkatayogi | Built with 💻 & 🚀</p>", unsafe_allow_html=True)
