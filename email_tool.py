
from email_client import EmailClient
from email_message import EmailMessage
from response import Response
from task import Task

class EmailTool:
    def __init__(self, imap_server, smtp_server, email_address, password, important_domain):
        self.email_client = EmailClient(imap_server, smtp_server, email_address, password)
        self.email_client.connect_to_server()
        self.important_domain = important_domain

    def process_emails(self):
        emails = self.email_client.fetch_emails()
        for raw_email in emails:
            email = EmailMessage(raw_email)
            if email.is_important(self.important_domain):
                task = Task(email)
                print(task.task_description)
            response = Response(self.email_client)
            subject, body = response.draft_response(email)
            response.send_response(email.from_address, subject, body)

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    imap_server = os.getenv('IMAP_SERVER')
    smtp_server = os.getenv('SMTP_SERVER')
    email_address = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('EMAIL_PASSWORD')
    important_domain = os.getenv('IMPORTANT_DOMAIN')

    tool = EmailTool(imap_server, smtp_server, email_address, password, important_domain)
    tool.process_emails()
    