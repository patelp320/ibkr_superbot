from ib_insync import IB, util
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage


def connect_ib():
    """Connect to the Interactive Brokers gateway or TWS."""
    host = os.getenv('IB_HOST', '127.0.0.1')
    port = int(os.getenv('IB_PORT', 7497))
    client_id = int(os.getenv('IB_CLIENT_ID', 1))
    ib = IB()
    ib.connect(host, port, clientId=client_id)
    return ib


def fetch_account_summary(ib: IB) -> str:
    """Fetch account summary as a string."""
    summary = ib.accountSummary()
    df = util.df(summary)
    return df.to_string()


def send_email(subject: str, body: str) -> None:
    """Send an email notification using SMTP details from the env."""
    msg = EmailMessage()
    msg['From'] = os.getenv('SMTP_USER')
    msg['To'] = os.getenv('EMAIL_TO')
    msg['Subject'] = subject
    msg.set_content(body)

    host = os.getenv('SMTP_HOST')
    port = int(os.getenv('SMTP_PORT', 587))
    user = os.getenv('SMTP_USER')
    password = os.getenv('SMTP_PASS')

    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        if user and password:
            smtp.login(user, password)
        smtp.send_message(msg)


def main() -> None:
    load_dotenv()
    ib = connect_ib()
    try:
        summary_text = fetch_account_summary(ib)
        send_email('IBKR Account Summary', summary_text)
    finally:
        ib.disconnect()


if __name__ == '__main__':
    main()
