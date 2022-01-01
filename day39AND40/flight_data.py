import datetime
import requests as req
import API_KEYS as ak
from pprint import pprint

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.ENDPOINT = ak.KIWI_SEARCH_ENDPOINT
        self.headers={
            "apikey":f"{ak.KIWI_API_KEY}"
        }

    def search_flights(self,IATA:str,lowestPrice:str) -> dict:
        date = datetime.date.today()+datetime.timedelta(days=1)
        today = f"{date.strftime('%d/%m/%Y')}"
        six_months_later = f"{(date + datetime.timedelta(days=(30*6))).strftime('%d/%m/%Y')}"

        params = {
            "fly_from":f"{IATA}",
            "date_from":today,
            "date_to":six_months_later,
            "price_from":0,
            "price_to":f"{lowestPrice}",
        }

        response = req.get(url=self.ENDPOINT,params=params,headers=self.headers)

        response.raise_for_status()

        return response.json()