import pandas
import streamlit as st
import pandas as ps

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo2.jpg", width=500)


with col2:
    st.title("Istvan Löffler")
    content = """Hi! I am Istvan Löffler a beginner programmer and mechatronics engineer. I am currently conducting my studies in BME - Technologycal University of Budapest.
    I have knowledge of warring degree from beginner to upper-intermediate, about the following programs:
    C, C++, C#, Python, Py-Django, Py-OpenCV, Py-Mediapipe, Labview, Matlab, SolidWorks, SolidEdge and FPWIN Pro7"""
    st.info(content)

st.write('<p style="color:black; font-size:20px;"'
         '><b>Below you can find some of the apps I built in Python. Feel free to contact me.<b></p>',
         unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
