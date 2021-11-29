# ------------------------PIXELA
# PIXELA WEBSITE https://pixe.la/
# PIXELA DOCUMENTATION https://docs.pixe.la/
# PYTHON REQUEST DOCUMENTATION https://docs.python-requests.org/en/latest/api/

import requests 
import datetime
import os

import API_KEYS as ak

PIXELA__ENDOPOINT="https://pixe.la/v1/users" #create an user
GRAPH_ENDPOINT=f"{PIXELA__ENDOPOINT}/{ak.USERNAME}/graphs"
PIXEL_ENDPOINT=f"{GRAPH_ENDPOINT}/{ak.MY_GRAPH_ID}"

params = {
    "token":ak.MY_TOKEN,
    "username":ak.USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
    }
"""1-Create your user account"""
#response = requests.post(url=PIXELA_CREATE_USER_ENDOPOINT,json=params)
#print(response.text)
#{"message":"Success.","isSuccess":true}

"""2-Create a graph definition"""
graph_config = {
    "id":ak.MY_GRAPH_ID,
    "name":"Coding graph",
    "unit":"hours",
    "type":"float",
    "color":"ajisai"
    }
headers={
    "X-USER-TOKEN":ak.MY_TOKEN
}
#response=requests.post(url=GRAPH_ENDPOINT,json=graph_config,headers=headers)
#print(response.text)
#{"message":"Success.","isSuccess":true}

"""3-Get the graph!"""
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph !
# This is also /v1/users/<username>/graphs/<graphID> API.
# finally .html
# in my case https://pixe.la/v1/users/rychy248/graphs/graph1.html

"""4-Post value to the graph"""

pixel_config={
    "date":"20211129",
    "quantity":"2"
}
headers={
    "X-USER-TOKEN":ak.MY_TOKEN
}
#response = requests.post(url=PIXEL_ENDPOINT,json=pixel_config,headers=headers)
#print(response.text)
"""5-Browse again!"""
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph !
# This is also /v1/users/<username>/graphs/<graphID> API.
# finally .html
# in my case https://pixe.la/v1/users/rychy248/graphs/graph1.html

"""6-You can also find out more about."""
# You can get more information by adding .html to the end of the URL on
# Step.6 at it in your browser! (https://pixe.la/v1/users/a-know/graphs/test-graph.html)
class GraphCodignManage():
    def add_pixel(self,date="YYYYMMDD",hours=1):
        """Add automatically hour dayli streak"""
        "DATE = YYYYMMDD"

        if date =="YYYYMMDD":
            today=datetime.date.today()
            date= f"{today.strftime('%Y%m%d')}"

        pixel_config={
            "date":date,
            "quantity":f"{hours}",
        }

        headers={
            "X-USER-TOKEN":ak.MY_TOKEN,
        }

        response = requests.post(url=PIXEL_ENDPOINT,json=pixel_config,headers=headers)
        print(response.text)

    def update_pixel(self,date="YYYYMMDD",hours=1):
        "DATE = YYYYMMDD"
        if date =="YYYYMMDD":
            today=datetime.date.today()
            date= f"{today.strftime('%Y%m%d')}"

        update_pixe_endpoint = f"{PIXEL_ENDPOINT}/{date}"

        pixel_config={
            "quantity":f"{hours}",
        }
        headers={
            "X-USER-TOKEN":ak.MY_TOKEN
        }
        response = requests.put(url=update_pixe_endpoint,json=pixel_config,headers=headers)
        print(response.text)

    def del_pixel(self,date="YYYYMMDD",last_days=None):
        "DATE = YYYYMMDD, if you set last_days, don't set the date"
        headers={
            "X-USER-TOKEN":ak.MY_TOKEN
        }
        
        def __del(end_point:str):
            response = requests.delete(url=end_point,headers=headers)
            print(response.text)

        today = datetime.date.today()
        if date =="YYYYMMDD" and last_days is not None: #del the last days seted
            i=0
            while last_days>i:
                day_del = today- datetime.timedelta(days=i)
                date = f"{day_del.strftime('%Y%m%d')}"
                del_pixel_endpoint = f"{PIXEL_ENDPOINT}/{date}"        
                __del(del_pixel_endpoint)
                i+=1
        elif date =="YYYYMMDD": #del today automatically
            date= f"{today.strftime('%Y%m%d')}"
            del_pixel_endpoint = f"{PIXEL_ENDPOINT}/{date}"        
            __del(del_pixel_endpoint)
        else:
            del_pixel_endpoint = f"{PIXEL_ENDPOINT}/{date}" #del an especific day
            __del(del_pixel_endpoint)

    def read_pixel(self,date="YYYYMMDD",last_days=None):
        "DATE = YYYYMMDD, if you set last_days, don't set the date"
        headers={
            "X-USER-TOKEN":ak.MY_TOKEN
        }
        
        def __read(end_point:str,date:str):
            response = requests.get(url=end_point,headers=headers)
            print(date,"->",response.text)

        today = datetime.date.today()
        if date =="YYYYMMDD" and last_days is not None: #read the last days seted
            i=0
            while last_days>i:
                day_read = today- datetime.timedelta(days=i)
                date = f"{day_read.strftime('%Y%m%d')}"
                del_pixel_endpoint = f"{PIXEL_ENDPOINT}/{date}"        
                __read(del_pixel_endpoint,date)
                i+=1
        elif date =="YYYYMMDD": #del today automatically
            date= f"{today.strftime('%Y%m%d')}"
            del_pixel_endpoint = f"{PIXEL_ENDPOINT}/{date}"        
            __read(del_pixel_endpoint,date)
        else:
            del_pixel_endpoint = f"{PIXEL_ENDPOINT}/{date}" #read an especific day
            __read(del_pixel_endpoint,date)

#grap_code = GraphCodignManage()
# grap_code.del_pixel(last_days=8)
# grap_code.add_pixel()
#grap_code.read_pixel(last_days=6)

# today = datetime.date.today()
# i=0
# while 15>i:
#     day_del = today- datetime.timedelta(days=i)
#     date = f"{day_del.strftime('%Y%m%d')}"
#     grap_code.add_pixel(date)
#     i+=1

def main(messague_flag=None):

    def __ask_date():
        correct_input=False
        while not correct_input:
            year=input("Type the desired year: ")
            try:
                year = int(year)
                if 2000 < year < 2100:
                    correct_input = True
                else:
                    raise ValueError("Type a year bettwen 2000 and 2100")
            except ValueError:
                print("Incorrect input")

        correct_input=False
        while not correct_input:
            month=input("Type the month of year: ")
            try:
                month = int(month)
                if 1 <= month <= 12:
                    correct_input = True
                else:
                    raise ValueError("Type a month between 1 and 12")
            except ValueError:
                print("Incorrect input")

        correct_input=False
        while not correct_input:
            day=input("Type a day of the month: ")
            try:
                day = int(day)
                test_date = datetime.date(year=year,month=month,day=day)
                correct_input = True
            except ValueError:
                print("Incorrect input")

        return f"{test_date.strftime('%Y%m%d')}"

    def __ask_hour()->float:
        correct_input=False
        while not correct_input:
            hours=input("Type the number of hour coding today: ")
            try:
                hours = float(hours)
                correct_input = True
            except ValueError:
                print("Incorrect input")
        return hours

    def __last_days()->int:
        correct_input= False
        while not correct_input:
            days=input("Type the number of last days: ")
            try:
                days = int(days)
                correct_input = True
            except ValueError:
                print("Incorrect input")
        return days

    def __ask_cotinue()->bool:
        correct_input= False
        while not correct_input:
            decition = input("Do you want exit?:\ntype 'yes' or 'y'")
            if decition.upper() in ["YES","Y","1","TRUE","T"]:
                decition = True
                correct_input = True
            elif decition.upper() in ["NOT","N","NO","FALSE","F","0"]:
                decition = False
                correct_input = True
            else:
                print("Incorrect input")
        return decition

    grap_code = GraphCodignManage()
    stop= False

    while not stop:
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")

        if messague_flag is not None:
            print(messague_flag["messague"])
            messague_flag=None
        choise=input("""
Visit your Tracking-dayli here: https://pixe.la/v1/users/rychy248/graphs/graph1.html 
    1-Add a pixel
    2-Update a pixel
    3-Delete a pixel (or group)
    4-Read a pixel (or group)
    5-exit
        Choise: """)
        try:
            option = int(choise)
            if option == 1:
                choise = "ADD"
            elif option == 2:
                choise = "UPDATE"
            elif option == 3:
                choise = "DELETE"
            elif option == 4:
                choise = "READ"
            elif option == 5:
                choise = "EXIT"

            raise ValueError
        except ValueError:
            if choise.upper() in ["ADD","A","ADD A PIXEL"]:
                today = input("Do you want set for today?\ntype 'yes' or 'not': ")
                if today.upper() in ["YES","Y"]:
                    grap_code.add_pixel(hours=__ask_hour())
                else:
                    grap_code.add_pixel(date=__ask_date(),hours=__ask_hour())
            elif choise.upper() in ["UPDATE","UPD","UP","U"]:
                today = input("Do you want update today?\ntype 'yes' or 'not': ")
                if today.upper() in ["YES","Y"]:
                    grap_code.update_pixel(hours=__ask_hour())
                else:
                    grap_code.add_pixel(date=__ask_date(),hours=__ask_hour())
            elif choise.upper() in ["DELETE","DEL","DE","D"]:
                last_days = input("Do you want delete a number of last days?\ntype 'yes' or 'not': ")
                if last_days.upper() in ["YES","Y"]:
                    grap_code.del_pixel(last_days=__last_days())
                else:
                    grap_code.del_pixel(date=__ask_date())
            elif choise.upper() in ["READ","RE","R"]:
                last_days = input("Do you want read a number of last days?\ntype 'yes' or 'not': ")
                if last_days.upper() in ["YES","Y"]:
                    grap_code.read_pixel(last_days=__last_days())
                else:
                    grap_code.read_pixel(date=__ask_date())
            elif choise.upper() in ["E","EXIT","EX"]:
                stop = True
                messague_flag={
                    "exist":True,
                    "messague":"User exit!",
                }
            else:
                messague_flag={
                    "exist":True,
                    "messague":"Wrong Option!",
                }
            if messague_flag is None:
                stop=__ask_cotinue()

main()