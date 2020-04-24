import smtplib
import login_info

class mail:
    def __init__(self, account_info):
        self.account = account_info

    def compose(self, subject, body):
        self.subject = subject
        self.body = body

    def send(self, recipients):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            self.msg = f'Subject: {self.subject}\n\n{self.body}'

            smtp.login(self.account[0], self.account[1])

            for recipient in recipients:
                smtp.sendmail(self.account[0], recipient, self.msg)
