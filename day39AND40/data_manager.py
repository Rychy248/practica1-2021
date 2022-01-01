import requests as req
import API_KEYS as ak
from pprint import pprint

class CitiesManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.ENDPOINT = ak.SHEETY_END_POINT
        self.rows = []
        self.headers={
            "Authorization":f"Bearer {ak.BEARER_AUTHENTICATION}"
        }

    def print_rows(self,updateRequired=False) -> None:
        def __dict(a_dict:dict):
            for key,value in a_dict.items():
                print(f"{key}, ".center(12),end="")
                if type(value)is dict:
                    __dict(value)
                else:
                    print(f"{value}".center(12),end=" - ")

        if len(self.rows) !=0 and not updateRequired:
            for row in self.rows:
                __dict(row)
        else:
            self.get()
            self.print_rows()

    def get(self)->list:
        # return [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},{'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42},{'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485},{'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 551},{'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95},{'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414},{'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240},{'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260},{'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 378},{'city': 'Guatemala', 'iataCode': 'GUA', 'id': 11, 'lowestPrice': 23}]
        response = req.get(url=self.ENDPOINT,headers=self.headers)
        response.raise_for_status()
        
        self.rows = []
        for row in response.json()["prices"]:
            self.rows.append(row)

        return response.json()["prices"]
        
    def post(self,city,iataCode,lowestPrice):
        """RESPONSE EXAMPLE
        {"price":{'city': 'Guatemala','iataCode': 'GTM','id': 12,'lowestPrice': 23}}
        """
        body={'price':{
                'city':f"{city}",
                'iataCode':f"{iataCode}",
                'lowestPrice':lowestPrice,
                }
            }
        response = req.post(url=self.ENDPOINT,json=body,headers=self.headers)
        response.raise_for_status()
        return response.json()

    def put(self,objID:int,city:str,iataCode:str,lowestPrice:str):
        """ RESPONSE EXAMPLE
        {'price':{'city': 'Guatemala','iataCode': 'GTM','lowestPrice': '23','id': 12}}
        """
        body={'price':{
            'city':f"{city}",
            'iataCode':f"{iataCode}",
            'lowestPrice':lowestPrice,
            }
        }
        response = req.put(url=f"{self.ENDPOINT}/{objID}",json=body,headers=self.headers)
        response.raise_for_status()
        return response.json()
        
    def delete(self):
        ENDPOINT_DEL = "https://api.sheety.co/7fd0f13c4e4454ad02cf937b00d576ce/day38PythonWay/workouts/[Object ID]"

class CustomersManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.ENDPOINT = ak.SHEETY_END_POINT_CUSTOMERS
        self.rows = []
        self.headers={
            "Authorization":f"Bearer {ak.BEARER_AUTHENTICATION}"
        }

    def print_rows(self,updateRequired=False) -> None:
        def __dict(a_dict:dict):
            for key,value in a_dict.items():
                print(f"{key}, ".center(12),end="")
                if type(value)is dict:
                    __dict(value)
                else:
                    print(f"{value}".center(12),end=" - ")

        if len(self.rows) !=0 and not updateRequired:
            for row in self.rows:
                __dict(row)
        else:
            self.get()
            self.print_rows()

    def get(self)->list:
        """
        response : {'sheet1': []}
        """
        # return [{'email': 'jorgeajrha@gmail.com',
        #      'firstName': 'Rychy',
        #      'id': 2,
        #      'lastName': 'Hernandez'},
        #     {'email': 'jorgeajrhh@gmail.com',
        #      'firstName': 'Rychy',
        #      'id': 3,
        #      'lastName': 'Gonzales'},
        #     {'email': 'brayanexploited100@gmail.com',
        #      'firstName': 'Brayan',
        #      'id': 4,
        #      'lastName': 'Cabrera'}]
        response = req.get(url=self.ENDPOINT,headers=self.headers)
        response.raise_for_status()
        
        print("\nCUSTOMERS: ",len(response.json()["sheet1"]))

        self.rows = []
        print("(",end="")
        for row in response.json()["sheet1"]:
            self.rows.append(row)
            print(f"{row['firstName']} {row['lastName']}, ",end="")
        print(")")

        return response.json()["sheet1"]
        
    def post(self,firstName:str,lastName:str,email:str):
        """RESPONSE EXAMPLE
        """
        body={'sheet1':{
                'firstName':f"{firstName}",
                'lastName':f"{lastName}",
                'email':f"{email}",
                }
            }
        response = req.post(url=self.ENDPOINT,json=body,headers=self.headers)
        response.raise_for_status()
        return response.json()

    def put(self,objID:int,firstName:str,lastName:str,email:str):
        """ RESPONSE EXAMPLE
        {'price':{'city': 'Guatemala','iataCode': 'GTM','lowestPrice': '23','id': 12}}
        """
        body={'sheet1':{
                'firstName':f"{firstName}",
                'lastName':f"{lastName}",
                'email':f"{email}",
                }
            }
        response = req.put(url=f"{self.ENDPOINT}/{objID}",json=body,headers=self.headers)
        response.raise_for_status()
        return response.json()

# cm = CustomersManager()
# print("GET response")
# pprint(cm.get())
