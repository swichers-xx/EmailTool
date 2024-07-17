
class Response:
    def __init__(self, email_client):
        self.email_client = email_client

    def draft_response(self, email):
        subject = f"Re: {email.subject}"
        body = f"Dear {email.from_address},\n\nThank you for your email. We will get back to you shortly.\n\nBest regards,\nYour Team"
        return subject, body

    def send_response(self, to_address, subject, body):
        self.email_client.send_email(to_address, subject, body)
    