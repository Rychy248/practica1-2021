#instaled librarys
from twilio.rest import Client
import API_KEYS as ak

class NotificationManager():
    #This class is responsible for sending notifications with the deal flight details.

    def sendMsg(self,messegue:str,num="50242090991"):
        account_sid = ak.ACOOUNT_SID
        auth_token = ak.AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                     body=messegue,
                     from_=ak.MY_NUMBER,
                     to=f'+{num}'
                 )
        print("\n\nNOTIFICATION SENDED, message sid: ",message.sid,"\nmsg:",messegue)
