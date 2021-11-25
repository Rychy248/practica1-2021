#logic librarys
import random
import datetime as dt
import pandas as pd
#email tools
import smtplib
from email.mime.text import MIMEText
#--- own modules
import mail_credentials as mc

def __get_a_quote():
    quote = ""
    with open("quotes.txt","r") as file:
        string = file.read()
        string = string.strip()
        quotes = string.split("\n")
        quote = quotes[random.randint(0,len(quotes)-1)]

    return quote

def __get_current_year():
    now = dt.datetime.now()
    return now.year
def __get_current_month():
    now = dt.datetime.now()
    return now.month
def __get_current_day():
    now = dt.datetime.now()
    return now.day

def age(born_year=1990):
    age = 0
    now = dt.datetime.now()
    age = __get_current_year() - born_year

    return str(age)

def print_dict(dict_d):
    index = 0
    for key, value in dict_d.items():
        index += 1
        print("index=",index,"--",key,":",value)
    print("\n"*3)


def get_birthdays():
    "Return the birthdays, data or None"
    def __create_file():
        with open("birthdays.csv", "w") as file:
            file.write("sex,name,email,year,month,day\nWrite your data here!")

    birthdays = {}

    try:
        #data_frame = pd.read_csv("birthdays.csv")
        data_frame = pd.read_csv("birthdays.csv")

        if data_frame['sex'][0] == "Write your data here!":
            raise pd.errors.EmptyDataError
        #it's like SELECT * FROM data_frame WHERE month==__current_month AND day==__currente_Day;
        birthdays = data_frame[
            (data_frame['month']==__get_current_month()) & 
            (data_frame['day']==__get_current_day())
        ]
        
        if len(birthdays.index) <= 0: #num of rows
            birthdays = None

    except FileNotFoundError:
        __create_file()
        get_birthdays()
    except pd.errors.EmptyDataError:
        print("Write your data into 'birthday.csv'")
    
    return birthdays

def __get_letter(age,name,quote,sex):
    LETTER_OPTIONS = ["letter_1_","letter_2_","letter_3_"]
    letter_selected = str(random.choice(LETTER_OPTIONS))
    letter = ""

    with open(f"letter_templates/{letter_selected}{sex}.txt","r") as file:
        letter = file.read()
        letter = letter.replace("[AGE]",f"{age}")
        letter = letter.replace("[NAME]",f"{name}")
        letter = letter.replace("[QUOTE]",f"{quote}")

    return letter

def send_mail(mail_body,e_mail):
    """Send a happy birthday, mail"""

    with smtplib.SMTP(host=mc.HOST,port=mc.PORT) as server_mail:
        server_mail.starttls() #encrypted protocol
        server_mail.login(user=mc.MAIL,password=mc.PASSWORD) 
        
        mail = MIMEText(mail_body)
        mail['Subject'] = "HAPPY BIRTHDAY!"
        mail['From'] = mc.MAIL
        mail['To'] = e_mail

        server_mail.sendmail(from_addr=mc.MAIL,to_addrs=e_mail, msg=mail.as_string())
        server_mail.close()

def main():
    birthdays = get_birthdays()

    if birthdays is not None:
        #rows = len(birthdays.index)
        #print(f"Are {rows} in birthday")
        persons = [{
                    "sex":birthdays.sex[i],
                    "name":birthdays.name[i],
                    "email":birthdays.email[i],
                    "year":birthdays.year[i],
                    "month":birthdays.month[i],
                    "day":birthdays.day[i],
            } for i in birthdays.index]

        letter = ""
        for person in persons:
                letter = __get_letter(
                    age=age(person['year']),
                    name=person['name'],
                    quote=__get_a_quote(),
                    sex=person['sex'],
                    )
                send_mail(mail_body=letter,e_mail=person['email'])
    #else:
    #    print("Nobody is in birthday")


main()