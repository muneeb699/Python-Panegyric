# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 17:24:26 2016

@author: Muneeb ul Hassan
"""

from datetime import datetime, time, date, timedelta
import smtplib
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.text import MIMEText
host = "smtp.gmail.com"
port = 587
username = "umroayar24@gmail.com"
password = "Hatimtai92!"
email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()

class Users():
    user_details = []
    msgs = []
    email_details = []
    base_msg = "ahai"
    
    def add_user(self, name, email=None):
        name = name[0].upper() + name[1:].lower()
        details = {
            "name" : name,
        }
        today = datetime.today()
        date_txt = '{today.date}-{today.month}-{today.year}'.format(today=today)
        details['date'] = date_txt
        if email is not None:
            details['email'] = email
            self.user_details.append(details)
    def get_details(self):
        return self.user_details
    def make_msgs(self):
        if len(self.user_details)>0:
            for details in self.get_details():
                name = details['name']
                date = details['date']
                msgs = self.base_msg
                new_msg = msgs.format(
                    name = name,
                    date = date,
                )
                email_details = details.get('email')
                if email_details:
                    user_data = {
                            "email":email_details,
                            "msgs" : new_msg
                    }
                    self.email_details.append(user_data)
                else:
                    self.msg.append(new_msg)
            return self.msgs
        return []
    def send_email(self):
        self.make_msgs()
        if len(self.make_msgs)>0:
            for details in self.email_details:
                user_email = details['email']
                user_msg = details['msgs']
                try:
                    email_conn.login(username,password)
                    email_conn.quit()
                    msg = MIMEMultipart("alternative")
                    msg['Subject'] = "AI Class schedule"
                    msg["From"] =username
                    msg["To"] = user_email
                    msg_txt = "AI classes starting soon"
                    html_msg_txt = """\
                    <html>
                        <head></head>
                        <body>
                            <p>Hey! <br>
                                Checkout the link <a href='http//github.com/muneeb699'>muneeb699</a>
                            </p>
                        </body>
                    </html>
                    """
                    msg1 = MIMEText(msg_txt, 'plain')
                    msg2 = MIMEText(html_msg_txt,"html")
                    msg.attach(msg1)
                    msg.attach(msg2)
                    email_conn.sendmail(username,[user_email],msg.as_string())
                    email_conn.quit()
                except SMTPAuthenticationError:
                    print("Not login")
                except:
                    print("an error occured")
            return True
        return False
obj = Users()
obj.add_user("Muneeb",email='umroayar24@gmail.com')
obj.add_user("Muneeb",email='umroayar24@gmail.com')
obj.add_user("Muneeb",email='umroayar24@gmail.com')
obj.add_user("Muneeb",email='umroayar24@gmail.com')
obj.get_details()
obj.send_email()