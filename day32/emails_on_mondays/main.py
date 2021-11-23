import smtplib
import random
import datetime as dt
from email.mime.text import MIMEText

#--- own modules
import mail_credentials as mc

def line(g_num=80):
    """Print a line with guios (-).
    Default are 80, or you can set a lenght of them
    """
    print("-"*g_num)

def astherisc_str(string,ast_num=5):
    """Printe a text, between astheriscs (*)
    Default are 4, or you can set a lenght of them
    """
    print("*"*ast_num,string,"*"*ast_num)

def is_monday():
    """Return True if today is Monday"""
    answer = False
    now = dt.datetime.now()
    
    if now.weekday == 1:
        answer = True

    return answer

def send_mail():
    """Send a quote, to list of emails are in the file 'mail_credentials.py'"""
    line()
    astherisc_str("Mail sender, credentials")
    print(mc.MAIL)
    print(mc.PASSWORD)
    line()

    astherisc_str("Initial sending mails...",3)
    with smtplib.SMTP(host=mc.HOST,port=mc.PORT) as mail_connection:
        print("mail server conected")
        mail_connection.starttls()
        print("TLS protocol started")
        mail_connection.login(user=mc.MAIL,password=mc.PASSWORD) 
        print(f"User {mc.MAIL} logeed")

        quote = ""
        with open("quotes.txt","r") as file:
            string = file.read()
            string = string.strip()
            quotes = string.split("\n")
            quote = quotes[random.randint(0,len(quotes)-1)]

        ms=f"""Hi there! :)!

{quote}

Have a Good Monday :D!

Bye!

Att: Brayan Exploited"""
        messege = MIMEText(ms)
        messege['Subject'] = "HAPPY MONDAY!"
        messege['From'] = mc.MAIL
        messege['To'] = mc.MAILS_TO_SEND[0]

        print(f"Mail sended to:")

        mail_connection.sendmail(from_addr=mc.MAIL,to_addrs=mc.MAILS_TO_SEND, msg=messege.as_string())
        for mail in mc.MAILS_TO_SEND:
            print(" "*5,mail,"...")

        mail_connection.close()
        astherisc_str("Close",4)
        line()

if is_monday():
    send_mail()
else:
    print("Today isn't monday")
