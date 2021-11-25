import smtplib
import requests
import time
from email.mime.text import MIMEText
from datetime import datetime

def __create_file(file_name,msg):
    with open(f"{file_name}", "w") as file:
        file.write(f"{msg}")

try:
    import my_position as mp
except ModuleNotFoundError:
    __create_file("my_position.py","#put your coordenates here\nMY_LAT = 0\nMY_LNG = 0")
    import my_position as mp
finally:
    if mp.MY_LAT==0 and mp.MY_LNG==0:
        raise ValueError("Coordenates are wrong check the file 'my_position.py'")

try:
    import mail_credentials as mc
except ModuleNotFoundError:
    file_name= "mail_credentials.py"
    msg='# fill your credentials \nMAIL=""\nPASSWORD=""\nHOST=""\nPORT=""'
    __create_file(file_name=file_name,msg=msg)
    import mail_credentials as mc
finally:
    if  mc.MAIL=="" and mc.PASSWORD==""and mc.HOST=="" and mc.PORT=="":
        raise ValueError("Fill your credentials into 'mail_credentials.py'")

#-----logic's program vvvvv
def __set_surise_sunset_time():
    global sunrise,sunset
    
    parameters = {
        "lat": mp.MY_LAT,
        "lng": mp.MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) -6
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 6
    if sunset < 0:
        sunset += 24 #posible the sunset it's  less than 6, and it's mean a wrong situation
        #the solution is adding 24 hour, who ronds araound 19 or 24

def __set_iss_position():
    global iss_latitude,iss_longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

def __iss_close_to_me():
    "Your position is within +5 or -5 degrees of the ISS position."
    __set_iss_position()
    # 3 <= a <= 6 | possible a values are: 3, 4, 5, 6
    near_latitude = True if mp.MY_LAT-5 <= iss_latitude <= mp.MY_LAT+5 else False
    near_longitude = True if mp.MY_LNG-5 <= iss_longitude <= mp.MY_LNG+5 else False

    return True if near_latitude and near_longitude else False

def __its_currently_dark():
    "Return if the sky in your position is dark "
    __set_surise_sunset_time()
    time_now = datetime.now()
    
    is_so_morgin = True if sunrise > time_now.hour else False
    is_night = True if sunset < time_now.hour else False

    return True if is_so_morgin or is_night else False

def __send_mail():
    """Send a notification"""

    with smtplib.SMTP(host=mc.HOST,port=mc.PORT) as server_mail:
        server_mail.starttls() #encrypted protocol
        server_mail.login(user=mc.MAIL,password=mc.PASSWORD) 
        
        to_me = "jorgeajrha@gmail.com"
        mail = MIMEText("Look at the sky it's the ISS over your head")
        mail['Subject'] = "ISS is over you!"
        mail['From'] = mc.MAIL
        mail['To'] = to_me

        server_mail.sendmail(from_addr=mc.MAIL,to_addrs=to_me, msg=mail.as_string())

def main():
    if __iss_close_to_me() and __its_currently_dark():
            print("ISS is close to me!")
            __send_mail()
            print("mail sended, it's currently dark")
    else:
        print("ISS is not close to me!",end=" ")
        if __its_currently_dark():
            print("and :( it's currently dark")
        else:
            print("But don't worry it's not currently dark")
    time.sleep(60)
    main()

main()