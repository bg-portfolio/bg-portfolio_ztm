import smtplib
from email.message import EmailMessage as EM
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "FleyFawkes"
email["to"] = "<email_receiver>"
email["subject"] = "<your_subject_here>"

email.set_content(hmtl.substitute(name="Jon"), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("<your_email>", "<your_password>")
    smtp.send_message(email)
