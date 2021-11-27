# API WEBhttps://home.openweathermap.org/users/sign_up\n
# WEB: https://home.openweathermap.org/

# slice python documentation https://stackoverflow.com/questions/509211/understanding-slice-notation
# w3shool python slice referemce https://www.w3schools.com/python/ref_func_slice.asp

import requests
import open_wather_API_KEY as cred

import os
from twilio.rest import Client

def send_msm(messegue):
    account_sid = cred.ACOOUNT_SID
    auth_token = cred.AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body=f"Hello there, {messegue}! att Rychy :)!",
                     from_=cred.MY_NUMBER,
                     to='+50242090991'
                 )
    print(message.sid)

def main():
    parameters = {
        "lat":15.173806,
        "lon":-90.939296,
        "appid":cred.API_KEY,
        "exclude":"current,minutely,daily",
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?",params=parameters)
    response.raise_for_status()
    wather_data = response.json()

    weather_12 = [(
        hour["weather"][0]["id"],
        hour["weather"][0]["main"],
        hour["weather"][0]["description"]
        ) for hour in wather_data["hourly"][:13]]

    bring_un_ambrella = False

    for i in range(0,len(weather_12)-1):
        bring_un_ambrella = True if weather_12[i][0] < 700 else False
    messegue = ""
    if bring_un_ambrella:
        messegue = "Bring an umbrella ☔!"
    else:
        messegue = "Don't bring an umbrella 🌤!"
    
    send_msm(messegue)

main()