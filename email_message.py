
class EmailMessage:
    def __init__(self, raw_email):
        self.raw_email = raw_email
        self.subject = raw_email['subject']
        self.from_address = raw_email['from']
        self.body = self.parse_email()

    def parse_email(self):
        if self.raw_email.is_multipart():
            for part in self.raw_email.iter_parts():
                if part.get_content_type() == 'text/plain':
                    return part.get_payload(decode=True).decode()
        else:
            return self.raw_email.get_payload(decode=True).decode()

    def is_important(self, domain):
        return domain in self.from_address
    