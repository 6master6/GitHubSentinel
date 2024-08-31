import smtplib
from email.mime.text import MIMEText

class NotificationSystem:
    def __init__(self, config):
        self.email_config = config.get("email")

    def send_notifications(self, report):
        msg = MIMEText(report)
        msg["Subject"] = "GitHub Repository Updates"
        msg["From"] = self.email_config["from"]
        msg["To"] = self.email_config["to"]

        with smtplib.SMTP(self.email_config["smtp_server"]) as server:
            server.login(self.email_config["username"], self.email_config["password"])
            server.sendmail(self.email_config["from"], [self.email_config["to"]], msg.as_string())
