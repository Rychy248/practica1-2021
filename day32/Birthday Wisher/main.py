import smtplib
import mail_credentials as mc

def line():
    print("-"*80)

print(mc.MAIL)
print(mc.PASSWORD)
line()

def hard_method():
    # --
    mail_connection = smtplib.SMTP(host=mc.HOST,port=mc.PORT)
    #Simple mail transfer protocol
    print("mail conected")
    mail_connection.starttls()
    #Transport Layer Security
    # Starttls, Puts the connection to the SMTP server into TLS mode.
    # If there has been no previous EHLO or HELO command this session, this method tries ESMTP EHLO first.
    # If the server supports TLS, this will encrypt the rest of the SMTP session. If you provide the keyfile and certfile parameters, the identity of the SMTP server and client can be checked. This, however, depends on whether the socket module really checks the certificates.
    print("TLS started")
    mail_connection.login(user=mc.MAIL,password=mc.PASSWORD) 
    print("Loged")

    #for add subject the email just add subject into the messegue
    ms="""Subject:Hi there!\n\n
    Hi there! :)
    i'm happy to gretting you!

    By! Att: Brayan Exploited
    """

    mail_connection.sendmail(from_addr=mc.MAIL,to_addrs="jorgeajrhh@gmail.com", msg=ms)
    print("Mail sended")
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

        ms="""Subject:Hi there!\n\n
        Hi there! :)
        i'm happy to gretting you!

        By! Att: Brayan Exploited
        """
        mail_connection.sendmail(from_addr=mc.MAIL,to_addrs="jorgeajrhh@gmail.com", msg=ms)
        print("Mail sended")
        mail_connection.close()
        print("Close")
        line()

hard_method()
with_mode()