# OPENAI API web https://openai.com/blog/openai-api/
# Sheety API web https://sheety.co/

import requests as req
import os
from datetime import datetime as dt

import API_KEYS as sky

class NutritionAPI():
    """Class who manage acces to NutrionixAPI"""
    # Nutriotion WEB API https://www.nutritionix.com/business/api

    def __init__(self) -> None:
        self.data = None

    def post(self):
        GENDER = ["male","female"]
        gender=0
        weight_kg=75
        height_cm=169
        age=21

        def __ask_data():
            nonlocal gender, weight_kg,height_cm, age
            correct_input = False
            while not correct_input:
                try:
                    gender=int(input("Tell me your gender, male=0 or female=1: "))
                    correct_input = True
                except ValueError:
                    print("You need to write 1 or 0")

            correct_input = False
            while not correct_input:
                try:
                    weight_kg=float(input("Tell me your weight in kg: "))
                    correct_input = True
                except ValueError:
                    print("You need to write a float")

            correct_input = False
            while not correct_input:
                try:
                    height_cm=float(input("Tell me your height in cm: "))
                    correct_input = True
                except ValueError:
                    print("You need to write float")

            correct_input = False
            while not correct_input:
                try:
                    age=float(input("Tell me your age years: "))
                    correct_input = True
                except ValueError:
                    print("You need to write an integer")

        q = input("Tell me wich excersises you did: ")
        ask_flag=False

        correct_input = False
        while not correct_input:
            try:
                decition = int(input("Do you want set WEITHG_KG, HEIGHT_CM and your AGE?\n1=yes, or 0=false: "))
                ask_flag = False if 0 >= decition  or decition  >=2  else True
                correct_input = True
            except ValueError:
                print("You need to write 1 or 0")

        if ask_flag:
            __ask_data()

        endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        headers={
            "Content-Type":"application/json",
            "x-app-id":sky.NUTRION_APLICATION_ID,
            "x-app-key":sky.NUTRION_API_KEY,
        }
        params={
            "query":q,
            "gender":GENDER[gender],
            "weight_kg":weight_kg,
            "height_cm":height_cm,
            "age":age,

        }
        response = req.post(url=endpoint,headers=headers,json=params,)
        response.raise_for_status()
        self.data = response.json()["exercises"]
        self.__data()
        return self.data

    def __data(self):
        data = []
        for excercise in self.data:
            data.append({
                "excercise":excercise["name"],
                "calories":excercise["nf_calories"],
                "duration in mins":excercise["duration_min"],
            })
        self.data = data

    def print_data(self)->None:
        def __print_dict(d:dict):
            for key,value in d.items():
                print(key)
                if type(value) is dict:
                    __print_dict(value)
                if type(value) is list:
                    for item in value:
                        if type(item) is dict:
                            __print_dict(item)
                        else:
                            print("--",item)
                else:
                    print("--",value)
                    
        if self.data is not None:
            if type(self.data) is list:
                for data in self.data:
                    if type(data) is dict:
                        __print_dict(data)
                    else:
                        print("--",data)

class SheetyAPI():
    def __init__(self) -> None:
        self.ENDPOINT = "https://api.sheety.co/7fd0f13c4e4454ad02cf937b00d576ce/day38PythonWay/workouts"
        self.rows = []
        self.headers={
            "Authorization":f"Bearer {sky.BEARER_AUTHENTICATION}"
        }

    def print_rows(self):
        def __dict(a_dict:dict):
            for key,value in a_dict.items():
                print(key,": ",end="")
                if type(value)is dict:
                    __dict(value)
                else:
                    print(value,end=" - ")

        if len(self.rows) !=0:
            for row in self.rows:
                __dict(row)
                print(":)")
        else:
            self.get()
            self.print_rows()

    def get(self):
        response = req.get(url=self.ENDPOINT,headers=self.headers)
        response.raise_for_status()
        self.rows = []
        for row in response.json()["workouts"]:
            self.rows.append(row)
        return self.rows

    def post(self,duration:float,exercise:str,calories:float):
        current_time_date = dt.now()
        today = current_time_date.strftime("%y/%m/%d")
        current_time = current_time_date.strftime("%H:%M:%S")

        body={'workout':{
                'date': f"{today}",
                'time': f'{current_time}',
                'exercise': exercise,
                'duration': f"{duration}",
                'calories': f"{calories}",
                }
            }
        response = req.post(url=self.ENDPOINT,json=body,headers=self.headers)
        response.raise_for_status()
        print(f"today:{today}, exercise:{exercise}. ",response)

    def put(self):
        ENDPOINT_PUT  = "https://api.sheety.co/7fd0f13c4e4454ad02cf937b00d576ce/day38PythonWay/workouts/[Object ID]"

    def delete(self):
        ENDPOINT_DEL = "https://api.sheety.co/7fd0f13c4e4454ad02cf937b00d576ce/day38PythonWay/workouts/[Object ID]"



def main():
    nutrion = NutritionAPI()
    sheety = SheetyAPI()

    def __insert():
        excersices = nutrion.post()
        for e in excersices:
            sheety.post(
                duration=e["duration in mins"],
                exercise=e["excercise"],
                calories=e["calories"]
                )
    
    def __clear():
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")
    
    correct_input = False
    while not correct_input:
        try:
            option = int(input("""
            
0 - Exit of the program
1 - read
2 - insert

option.... """))
            if not (0 <= option <= 2):
                raise ValueError
            elif option == 0:
                __clear()
                correct_input = True
                print("Bye!")
            elif option == 1:
                __clear()
                sheety.print_rows()
            elif option == 2:
                __clear()
                __insert()
                
        except ValueError:
            __clear()
            print("You have to input a valid option, (0 to 2)")


main()