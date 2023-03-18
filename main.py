from chat_bot import ChatBot
from wa_comm import TwilioBot
import time

if __name__=="__main__":
    chat_bots={}
    twilio=TwilioBot()

    while True:
        print("Entering main loop")
        unread_list=twilio.get_pending_messages()
        if len(unread_list)==0:
            time.sleep(3)
            continue

        contents=twilio.parse_pending_messages(unread_list)

        responses={}
        for phone_number in contents.keys():
            message_content=contents[phone_number]
            if phone_number not in chat_bots:
                chat_bots[phone_number]=ChatBot()
            chat_bot=chat_bots[phone_number]

            if message_content=="Start":
                intro_message=chat_bot.get_intro_message()
                responses[phone_number]=intro_message
                continue

            response=chat_bot.get_response(message_content)
            responses[phone_number]=response
        
        for phone_number in responses.keys():
            message_content=responses[phone_number]
            twilio.send_message(phone_number, message_content)
        
        time.sleep(3)
        print("Main loop done")
