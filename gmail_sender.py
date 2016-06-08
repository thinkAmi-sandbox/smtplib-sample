import sys
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

ACCOUNT = "example@gmail.com"
ALIAS = "example+alias@gmail.com"
PASSWORD = "passw0rd"


def create_message(subject):
    msg = MIMEText("Body: Hello world!")
    msg["Subject"] = subject
    msg["From"] = ACCOUNT
    msg["To"] = ALIAS
    msg["Date"] = formatdate(localtime=True)
    return msg


def sendmail_with_ehlo_using_smtp():
    msg = create_message(sys._getframe().f_code.co_name)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(ACCOUNT, PASSWORD)

    s.sendmail(ACCOUNT, ALIAS, msg.as_string())
    s.quit()
    
    print("finished: {}".format(sys._getframe().f_code.co_name))


def sendmail_without_ehlo_using_smtp():
    msg = create_message(sys._getframe().f_code.co_name)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(ACCOUNT, PASSWORD)

    s.sendmail(ACCOUNT, ALIAS, msg.as_string())
    s.quit()
    
    print("finished: {}".format(sys._getframe().f_code.co_name))


def sendmail_using_smtp_ssl():
    msg = create_message(sys._getframe().f_code.co_name)

    # using default port: 465
    s = smtplib.SMTP_SSL("smtp.gmail.com")
    s.login(ACCOUNT, PASSWORD)

    s.sendmail(ACCOUNT, ALIAS, msg.as_string())
    s.quit()
    
    print("finished: {}".format(sys._getframe().f_code.co_name))


def send_message_using_smtp_ssl():
    msg = create_message(sys._getframe().f_code.co_name)

    s = smtplib.SMTP_SSL("smtp.gmail.com")
    s.login(ACCOUNT, PASSWORD)

    s.send_message(msg)
    s.quit()

    print("finished: {}".format(sys._getframe().f_code.co_name))


if __name__ == "__main__":
    sendmail_with_ehlo_using_smtp()
    sendmail_without_ehlo_using_smtp()
    sendmail_using_smtp_ssl()
    send_message_using_smtp_ssl()

