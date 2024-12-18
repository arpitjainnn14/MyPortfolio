"""
standard python library for creating email client session
ssl library us creating a secure context for websites.
"""
import smtplib,ssl

def send_email(message):
    #default values for gmail
    host="smtp.gmail.com"
    port=465

    #email address you registered the app password at.
    username="arpitj1414@gmail.com"
    #email address at which you want to receive emails
    receiver="arpitj1414@gmail.com"
    #password of the app created in apps password section of the id
    password="atma tpfq awqz cjod"
    
    #this holds the secure context for sending emails securely
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)