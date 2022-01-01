import smtplib
import random
import datetime as dt
from email.mime.text import MIMEText

#--- own modules
import API_KEYS as mc
class MailManager():
    def line(self,g_num=80):
        """Print a line with guios (-).
        Default are 80, or you can set a lenght of them
        """
        return ("-"*g_num)

    def astherisc_str(self,string,ast_num=5):
        """Printe a text, between astheriscs (*)
        Default are 4, or you can set a lenght of them
        """
        return (f'{"*"*ast_num} {string} {"*"*ast_num}')

    def is_monday(self):
        """Return True if today is Monday"""
        answer = False
        now = dt.datetime.now()

        if now.weekday == 1:
            answer = True

        return answer

    def send_mail(self,mails:list,flight:dict):
        """Send a mail to our customers '"""
        def flights_str(fligths:list):
            str_result = ""
            for flight in fligths:
                str_result += f"\n{self.line(20)}\n{flight}\n{self.line(20)}"

            return str_result

        self.astherisc_str("Mail sender, credentials")
        self.line()

        self.astherisc_str("Initial sending mails...",3)
        with smtplib.SMTP(host=mc.HOST,port=mc.PORT) as mail_connection:
            print("\n\n")
            print(self.line(),"\n")
            print(f"Mail server conected")
            mail_connection.starttls()
            print("TLS protocol started")
            mail_connection.login(user=mc.MAIL,password=mc.PASSWORD) 
            print(f"User {mc.MAIL} logeed")

            ms_body = ""
            ms_body+=f"\n{self.astherisc_str('Cheapest flight')}"
            ms_body+=f"\n{flight['cheapest_flight']}"
            ms_body+= "\n"
            ms_body+=f"\n{flights_str(flight['cheapers_flights'])}"
            ms_body+= "\n"
            ms_body+=f"\nHave a Good Day :D!"
            ms_body+= "\n"
            ms_body+=f"\nBye!"
            ms_body+= "\n"
            ms_body+=f"\nAtt: Brayan Exploited"
            
            for user in mails:
                ms_head=f"Hi {user['firstName']} {user['lastName']}! :)!\n"
                messege = MIMEText(f"{ms_head} {ms_body}")
                messege['Subject'] = "Cheaper Flight Notification!"
                messege['From'] = mc.MAIL
                messege['To'] = user['email']

                mail_connection.sendmail(from_addr=mc.MAIL,to_addrs=user['email'], msg=messege.as_string())
                print(f"Mail sended to:")
                print(" "*5,user['email'],"...")

            mail_connection.close()
            print(self.astherisc_str("Mail server conection closed...",4))
            print(self.line(),"\n")
