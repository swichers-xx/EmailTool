
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import policy
from email.parser import BytesParser

class EmailClient:
    def __init__(self, imap_server, smtp_server, email_address, password):
        self.imap_server = imap_server
        self.smtp_server = smtp_server
        self.email_address = email_address
        self.password = password

    def connect_to_server(self):
        self.imap_conn = imaplib.IMAP4_SSL(self.imap_server)
        self.imap_conn.login(self.email_address, self.password)
        self.smtp_conn = smtplib.SMTP_SSL(self.smtp_server)
        self.smtp_conn.login(self.email_address, self.password)

    def fetch_emails(self, mailbox='inbox'):
        self.imap_conn.select(mailbox)
        status, messages = self.imap_conn.search(None, 'ALL')
        email_ids = messages[0].split()
        emails = []
        for email_id in email_ids:
            status, msg_data = self.imap_conn.fetch(email_id, '(RFC822)')
            msg = BytesParser(policy=policy.default).parsebytes(msg_data[0][1])
            emails.append(msg)
        return emails

    def send_email(self, to_address, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        self.smtp_conn.sendmail(self.email_address, to_address, msg.as_string())
    