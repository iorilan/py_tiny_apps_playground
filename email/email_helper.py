import smtplib, ssl
import email
from email.header import decode_header
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib

def ping(username, password, smtp, port=587):
    with smtplib.SMTP(host=smtp, port=port) as server:
        server.starttls()
        server.login(username, password)
        print('login success')


def send_email(username, password, receiver, mail, smtp, port=587):
    
    msg = MIMEMultipart()
    msg['From']=username
    msg['To']=receiver
    msg['Subject']=mail['title']
    # body_format: plain/html
    msg.attach(MIMEText(mail['body'],mail['body_format']))
    if 'attachment_file' in mail :
        for file in mail['attachment_file']:
            # f: [path, application, octet-stream]
            with open(file[0],'rb') as atta:
                part = MIMEBase(file[1],file[2])
                part.set_payload(atta.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition",f'attachment; filename= {file[0]}')

                msg.attach(part)
    txt=msg.as_string()

    with smtplib.SMTP(host=smtp, port=port) as server:
        server.starttls()
        print('login...')
        server.login(username, password)
        print('sending...')
        server.sendmail(username,receiver,txt)
        print('sent')

def check_inbox(username, password,top=10):
    mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
    print('login...')
    mail.login(username, password)
    mail.list()
    print('checking inbox...')
    selected= mail.select('inbox')
    print(selected[0])
    messageCount=int(selected[1][0])

    
    for i in range(messageCount, messageCount - top, -1):
        data = mail.fetch(str(i), '(RFC822)')[1]
        for part in data:
            if isinstance(part, tuple):
                msg = email.message_from_bytes(part[1])
                # print(msg.keys())
                # return
                print('----------------Mail--------------------')
                for key in [ 'subject', 'to', 'from','date']:
                    print (f'{key}:{msg[key]}')
    
    mail.logout()
    print('logged out...')