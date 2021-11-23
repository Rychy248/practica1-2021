import smtplib
from email.mime.text import MIMEText

#--- own modules
import mail_credentials as mc

def line():
    print("-"*80)

print(mc.MAIL)
print(mc.PASSWORD)
line()

def hard_method():
    mail_connection = smtplib.SMTP(host=mc.HOST,port=mc.PORT) #Simple mail transfer protocol
    print("mail conected")
    mail_connection.starttls() #Transport Layer Security # Starttls, Puts the connection to the SMTP server into TLS mode.
    print("TLS started")
    mail_connection.login(user=mc.MAIL,password=mc.PASSWORD) 
    print("Loged")

    #for add subject the email just add subject into the messegue
    ms="""
    Hi there! :)
    I'm rychy, and i'm trygin to send you a messegue from
    my pc with python, i don't now, why, it's not possible
    end it's sending into spam, i hate it, but i don't now how
    solve it!

    Please Help Me!

    By! Att: Brayan Exploited
    """
    email_to_send = "jorgeajrhh@gmail.com"
    messege = MIMEText(ms)
    messege['Subject'] = "Hi i'm testing!"
    messege['From'] = mc.MAIL
    messege['To'] = email_to_send

    mail_connection.sendmail(from_addr=mc.MAIL,to_addrs=[email_to_send], msg=messege.as_string())

    print(f"Mail sended: [{email_to_send}]")
    mail_connection.close()
    print("Close")
    line()

def with_mode():
    print("usign with for smtplib")
    with smtplib.SMTP(host=mc.HOST,port=mc.PORT) as mail_connection:
        print("mail conected")
        mail_connection.starttls()

        print("TLS started")
        mail_connection.login(user=mc.MAIL,password=mc.PASSWORD) 
        print("Loged")

        ms="""
        Hi there! :)
        I'm rychy, and i'm trygin to send you a messegue from
        my pc with python, i don't now, why, it's not possible
        end it's sending into spam, i hate it, but i don't now how
        solve it!

        Please Help Me!

        By! Att: Brayan Exploited
        """
        email_to_send = "jorgeajrhh@gmail.com"
        messege = MIMEText(ms)
        messege['Subject'] = "Hi i'm testing!"
        messege['From'] = mc.MAIL
        messege['To'] = email_to_send

        mail_connection.sendmail(from_addr=mc.MAIL,to_addrs=[email_to_send], msg=messege.as_string())

        print(f"Mail sended: [{email_to_send}]")
        mail_connection.close()
        print("Close")
        line()

#hard_method()
#with_mode()