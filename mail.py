import smtplib, ssl
#import login_info
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import numpy as np

class mail:
    def __init__(self, account_info):
        """
        account_info: dict with keys 'username', 'password'
        """
        self.account = account_info

    def compose(self, subject, body):
        """
        body: dictionary with keys 'html', 'plaintext'
        """
        self.message = MIMEMultipart("alternative")
        self.message['subject'] = subject

        if 'plaintext' in body:
            self.message.attach(MIMEText(body['plaintext'], "plain"))
        if 'html' in body:
            self.message.attach(MIMEText(body['html'], "html"))

    def send(self, recipient):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            self.message['From'] = self.account['username']
            self.message["To"] = recipient

            smtp.login(self.account['username'], self.account['password'])
            smtp.sendmail(self.account['username'], recipient, self.message.as_string())
