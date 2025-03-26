
import streamlit as st
import plotly.express as px
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Anurag Venkatayogi | Data Portfolio", layout="wide")

# --- HERO SECTION ---
st.markdown("<h1 style='text-align: center;'>Anurag Venkatayogi</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Data Analyst | ML Enthusiast | Storyteller with Code</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Turning Data into Decisions. Visuals into Vision.</p>", unsafe_allow_html=True)

st.markdown("### Quick Links")
st.markdown("""
- [Resume](https://your-resume-link.com)
- [LinkedIn](https://www.linkedin.com/in/anuragvenkatayogi/)
- [GitHub](https://github.com/anurag-github)
- [Tableau Public](https://public.tableau.com/app/profile/anurag)
""")

# --- SKILLS DASHBOARD ---
st.markdown("## Skills Overview")

skills = {
    "Python": 95,
    "SQL": 90,
    "Tableau": 88,
    "Power BI": 85,
    "R": 80,
    "Machine Learning": 87,
    "Geospatial Tools": 75,
    "CRM Platforms": 70,
    "ETL & Data Prep": 90,
    "Data Visualization": 95
}

skill_df = pd.DataFrame({
    "Skill": list(skills.keys()),
    "Proficiency": list(skills.values())
})

fig = px.bar(skill_df, x="Proficiency", y="Skill", orientation="h", color="Proficiency", color_continuous_scale="Viridis")
st.plotly_chart(fig, use_container_width=True)

# --- PROJECTS SECTION ---
st.markdown("## Featured Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("AI-Powered Exam Cheating Detection System")
    st.markdown("- Used YOLOv8 & computer vision for unauthorized object detection.")
    st.markdown("- Integrated Wi-Fi/Bluetooth scanning for device alerts.")
    st.markdown("- Achieved 93% detection accuracy.")
    st.markdown("[GitHub](https://github.com/anurag-github/exam-proctoring)")

with col2:
    st.subheader("Airbnb Price Prediction & Chatbot")
    st.markdown("- Built ML model with 78% accuracy using regression techniques.")
    st.markdown("- Integrated AI chatbot for pricing and review analysis.")
    st.markdown("- Improved booking efficiency by 65%.")
    st.markdown("[GitHub](https://github.com/anurag-github/airbnb-chatbot)")

# --- CAREER TIMELINE ---
st.markdown("## Career Snapshot")

timeline_data = {
    "Year": ["2021", "2022", "2023", "2024"],
    "Position": ["Programmer Analyst Trainee", "Intern - DRDL", "Graduate Assistant Analyst", "MS Business Analytics (Ongoing)"]
}
timeline_df = pd.DataFrame(timeline_data)

timeline_fig = px.timeline(timeline_df, x_start="Year", x_end="Year", y="Position", color="Position", title="Career Timeline")
timeline_fig.update_yaxes(categoryorder="total ascending")
st.plotly_chart(timeline_fig, use_container_width=True)

# --- CONTACT SECTION ---
st.markdown("## Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thanks for reaching out! I'll get back to you soon.")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© 2025 Anurag Venkatayogi</p>", unsafe_allow_html=True)
