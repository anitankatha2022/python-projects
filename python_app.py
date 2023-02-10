from email.message  import  EmailMessage
from multiprocessing import context
from app2 import password
import ssl
import smtplib
email_sender='anitankatha310@gmail.com'
email_password=password
email_receiver='christinekarimi26@gmail.com'
subject='Do forget about family meeting'
body="""
The family meeting will be held on saturday
"""
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
    
    
  