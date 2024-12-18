# #creating a contact second page

# import streamlit as st
# from send_emails import send_email

# with st.form(key="contact_form"):
#     st.title("Contact me")
#     email=st.text_input("Enter your email address",placeholder="Your email...")
    
#     # this block of code defines the message sent by the user
#     message=st.text_area("Enter your message",placeholder="Your message...")
    
#     user_message=f"""\
# Subject: New email from {email}
    
# message sent to you: {message}
# {email}
# """
#     #when button is pressed this will execute
#     button=st.form_submit_button("Submit")
#     if button:
#         #above message will be called below and sent to the send email function which will work it's magic
#         send_email(user_message)
#         st.info("Your email was sent successfully!")


import streamlit as st
from send_emails import send_email

with st.form(key="contact_form"):
    st.title("Contact me")
    email = st.text_input("Enter your email address", placeholder="Your email...")
    
    # This block of code defines the message sent by the user
    message = st.text_area("Enter your message", placeholder="Your message...")
    
    user_message = f"""\
Subject: New email from {email}

Message sent to you:
{message}

From: {email}
"""
    # When the button is pressed this will execute
    button = st.form_submit_button("Submit")
    if button:
        # The above message will be called below and sent to the send_email function which will work its magic
        send_email(user_message)
        st.info("Your email was sent successfully!")
