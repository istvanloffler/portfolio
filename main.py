import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")


with col2:
    st.title("Istvan Löffler")
    content = """Hi! I am Istvan Löffler a programmer and mechatronics engineer. I am currently conducting my studies in BME - Technologycal University of Budapest.
    My specialties are: C, C++, C#, Python, Py-Django, Py-OpenCV, Py-Mediapipe, Labview, Matlab, SolidWorks, SolidEdge and FPWIN Pro7"""
    st.info(content)
