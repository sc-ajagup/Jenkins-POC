import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse
import os
from dotenv import load_dotenv

load_dotenv()


def send_email_smtp(subject, body, to_addresses, from_address="noreply@auriga.scryai.com"):
    # AWS SES SMTP credentials
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = ", ".join(to_addresses if isinstance(to_addresses, list) else [to_addresses])
    msg['Subject'] = subject

    # Email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_pass)  # Authenticate with SMTP credentials
            server.sendmail(from_address, to_addresses, msg.as_string())  # Send the email
        print("Email successfully sent!")
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send email via AWS SES SMTP.")
    parser.add_argument("to_addresses", type=str, help="Comma-separated list of recipient email addresses.")
    parser.add_argument("body", type=str, help="Body of the email.")
    parser.add_argument("target_branch", type=str, help="The target branch of the pull request.")
    parser.add_argument("source_branch", type=str, help="The source branch of the pull request.")
    parser.add_argument("pr_number", type=str, help="Pull request number.")

    args = parser.parse_args()

    to_addresses = [email.strip() for email in args.to_addresses.split(",")]
    subject = f"Jenkins: {args.target_branch} <- {args.source_branch} Pull Request: {args.pr_number}"

    body = args.body
    if send_email_smtp(subject, body, to_addresses):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
