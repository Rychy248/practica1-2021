import requests as req
import API_KEYS as ak
from pprint import pprint


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.ENDPOINT = ak.KIWI_QUERY_ENDPOINT
        self.headers={
            "apikey":f"{ak.KIWI_API_KEY}"
        }

    def search_Country(self,country:str) -> dict:
        """
        this method search de IATA code for the city seted()
        GET METHOD USED IN tequila api (created by Kiwi)
        """
        params = {
            "term":f"{country}",
            "location_types":"city",
            "active_only":True,
        }

        response = req.get(url=self.ENDPOINT,params=params,headers=self.headers)
        
        response.raise_for_status()
        return response.json()["locations"][0]["code"]