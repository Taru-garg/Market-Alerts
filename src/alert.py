from os import path
from typing import final
import uuid
import smtplib
from email.message import EmailMessage

class Alert():
    def __init__(self, *args):
        if len(args) == 1:
            with open(args[0], 'r') as file:
                if file.name.endswith('alrt'):
                    self.location = args[0]
                    self.email, self.marketName, self.triggerReason, self.price = (file.readline()).split(' ')
        elif len(args) == 4:
            self.email = args[0]
            self.price = args[1]
            self.triggerReason = args[2]
            self.marketName = args[3]

    def save_alert(self, folderpath='alerts/'):
        if self.email != '' and self.price != '':
            filename = folderpath + str(uuid.uuid1()) + '.alrt'
            try:
                with open(filename, 'w') as file:
                    file.write(f'{self.email} ')
                    file.write(f'{self.marketName} ')
                    file.write(f'{self.triggerReason} ')
                    file.write(f'{self.price}')
                return True
            except:
                return False
        return False

    def send_alert(self):
        alert_string = f'Price of {self.marketName} went {self.triggerReason} {self.price}'
        msg = EmailMessage()
        msg.set_content(alert_string)
        msg['Subject'] = 'Alert Triggered'
        msg['To'] = self.email
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('', '')
        s.send_message(msg)
        s.quit()