import email_helper as eh
import os
def send_mail(pwd):
    mail={}
    mail['title']='test'
    mail['body']="""
                    <html>
                        <body>
                        <p>Hi,<br>this is sample html sent <br>from email 
                            <a href="sample.link">sample</a> 
                        </p>
                        </body>
                    </html>
                """
    mail['body_format']='html'
    mail['attachment_file']=[[os.path.join('attachment','pdf1.pdf'),'application','octet-stream']]
    eh.send_email("test@hotmail.com",pwd,"test@hotmail.com",mail,'smtp-mail.outlook.com')



if __name__ == "__main__":
    print('password :')
    pwd=input()
    #eh.ping('test@hotmail.com',pwd,'smtp-mail.outlook.com')
    #send_mail(pwd)
    eh.check_inbox('test@hotmail.com',pwd,10)