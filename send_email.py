import smtplib
import config


host = "smtp.gmail.com"
subject = 'Send email by Python'
msg = config.msg

def send_email(subject, msg):
    """
    Function which send email
    :param subject: subject ofemail
    :param msg: text of email
    :return:
    """
    try:
        server = smtplib.SMTP(host + ':587')
        server.ehlo()
        server.starttls()
        server.login(config.work_email, config.password)
        # Message must be string from english characters and numbers. Russian text will except error.
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.work_email, config.receiver, message)
        server.quit()
        print('Success: Email sent!')
    except:
        print('Email failed to sent.')

if __name__ == '__main__':
    send_email(subject, msg)