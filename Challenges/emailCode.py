import  smtplib

SENDER_EMAIL = 'urbanjungleturban@gmail.com'
SENDER_PASSWORD = 'Test#123'

def send_email(recepient, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recepient, message)


send_email('simcarmelite.28@gmail.com', 'Deadpool3- Exclusive Trailer', "\n\n\nHey, Naughty boy! Caught you.")
