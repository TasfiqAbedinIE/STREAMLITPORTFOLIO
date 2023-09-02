import streamlit as st
# from send_email import send_mail
from send_email import send_mail

st.header("Contact US")

with st.form(key='emailForm'):
    user_email = st.text_input("Your Email Address")
    user_message = st.text_area("Your Message")
    user_message = user_message + '\n' + user_email
    button = st.form_submit_button("Submit")
    if button:
        send_mail(user_message)
        st.info("Your message is sent successfully")