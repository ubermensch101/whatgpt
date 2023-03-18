from twilio.rest import Client
from datetime import datetime

from datetime import date, timedelta

class TwilioBot:
    def __init__(self):
        self.client_list=[]

        account_sid = "ACa66d1ac3d7f531d1a4c478f1aa064a61"
        auth_token = "ffbcf8609ecdad803b7ab58c8bb9784e"
        self.client = Client(account_sid, auth_token)

        self.yesterday = date.today()-timedelta(1)
        self.phone_number="whatsapp:+14155238886"
    
    def get_pending_messages(self):
        messages_list=self.client.messages.list(date_sent_after=self.yesterday)
        client_list={}

        for message in messages_list:
            if message.from_==self.phone_number:
                phone_number=message.to
            else:
                phone_number=message.from_
            if phone_number in client_list:
                continue
            client_list[phone_number]=message
        
        unread_list=[]
        for phone_number in client_list.keys():
            message=client_list[phone_number]
            if message.direction=="inbound":
                unread_list.append(message)
        
        return unread_list
    
    def parse_pending_messages(self, unread_list):
        contents={}
        for message in unread_list:
            from_number=message.from_
            message_content=message.body
            contents[from_number]=message_content
        
        return contents
    
    def send_message(self, to_phone_number, message_text):
        message=self.client.messages.create(
            body=message_text,
            from_=self.phone_number,
            to=to_phone_number
        )
        print(message.sid)
