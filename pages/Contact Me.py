import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email form"):
    user_email = st.text_input("Your email address:")
    raw_message = st.text_area("Your message...")
    button = st.form_submit_button("Submit")

    message = f"""\
Subject: New email from: {user_email}
           
{raw_message} 
From: {user_email}
"""

    if button is True:
        send_email(message)
        st.info("Your message was sent successfully")

