"""
* APIs Required
*   Google Sheet Data Management - https://sheety.co/
*   Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/
*   Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
*   Twilio SMS API - https://www.twilio.com/docs/sms
"""
from data_manager import CitiesManager, CustomersManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from mail_manager import MailManager

from pprint import pprint


class Controller():
    def __init__(self) -> None:
        self.citiesData = CitiesManager()
        self.customersData = CustomersManager()
        self.fl_search = FlightSearch()
        self.flight_data = FlightData()

        self.cities = self.__get_cities()
        self.__search_save_IATA()

        self.customers = self.__get_customers()

    def search_fligths(self):
        #return {cheapers_flights:cheapers_flights, "cheapest_flight":cheapest_flight}
        fligths = self.__search_cheapers_flights()

        if fligths["cheapest_flight"] is not None:
            flag = True
            while flag:
                option = input("Do you want to send a Messegue to yor personal Number? y/n: ")
            
                if option.upper() in ["Y","YES","1","TRUE","T"]:
                    self.__send_notification_by_SMS(fligths["cheapest_flight"])
                    flag = False
                elif option.upper() in ["N","NO","NOT","FALSE","F","0"]:
                    flag = False
                else:
                    print("Option invalid, try again")

        return fligths

    def __get_cities(self) -> list:
        # get cities from sheete
        return self.citiesData.get()
    
    def __get_customers(self) -> list:
        # get cities from sheete
        return self.customersData.get()
    
    def save_customer(self):
        # Save Customer

        # firstName:str,lastName:str,email:str
        firstName = ""
        lastName = ""
        email = ""

        flag = True
        while flag:
            firstName = input("Type your first name: ")
            if len(firstName) <= 2:
                print(f"invalid, strange Name (To short {len(firstName)})")
            else:
                firstName = firstName.capitalize()
                flag = False
 
        flag = True
        while flag:
            lastName= input("Type your last name: ")
            if len(lastName) <= 2:
                print(f"invalid, strange Last Name (To short {len(lastName)})")
            else:
                lastName = lastName.capitalize()
                flag = False

        flag = True
        while flag:
            email= input("Type your email: ")
            if "@" not in email:
                print("email seted, haven't '@'")
                continue # restart this bucle, type email again
            
            parts = email.split("@")    #else
            if not len(parts) == 2:
                print("email invalid")
            elif not len(parts[0]) > 2:
                print("email seted is strange")
            elif "." not in parts[1]:
                print("email seted is strange")
                continue # restart this bucle, type email again

            domains = parts[1].split(".")   #else
            if not len(domains) >= 2:
                print("strange domain")
                continue # restart this bucle, type email again
            
            for dom in domains: #else
                if not len(dom) >= 2:
                    print("wrong domain in email")
                    break
            flag = False #catched the finally code
            
        return self.customersData.post(firstName,lastName,email);

    def __search_save_IATA(self):
        # search and save IATA code
        codesSearched = 0
        for city in self.cities:
            if city["iataCode"] == "":
                IATA_code = self.fl_search.search_Country(city["city"])
                pprint(f"country:{city['city']} IATA_CODE:{IATA_code}")
                self.citiesData.put(city["id"],city["city"],IATA_code,city["lowestPrice"])
                pprint("Data saved!")
                codesSearched+=1

        if codesSearched == 0:
            print("All cities are with IATA code!")

        print(f"Cities IATA code searched: {codesSearched}...\n")
    
    def __search_cheapers_flights(self) -> dict:
        # search cheapers flights
        cheapers_flights = []
        for city in self.cities:
            response = self.flight_data.search_flights(city["iataCode"],f"{city['lowestPrice']}")["data"]
            data = dict
            if len(response) > 0:
                data = {
                    'flyFrom':response[0]["flyFrom"],
                    'flyTo':response[0]["flyTo"],
                    'cityFrom':response[0]["cityFrom"],
                    'cityCodeFrom':response[0]["cityCodeFrom"],
                    'cityTo':response[0]["cityTo"],
                    'cityCodeTo':response[0]["cityCodeTo"],
                    'countryFrom':response[0]["countryFrom"],
                    'countryTo':response[0]["countryTo"],
                    'local_arrival':response[0]["local_arrival"],
                    'utc_arrival':response[0]["utc_arrival"],
                    'local_departure':response[0]["local_departure"],
                    'utc_departure':response[0]["utc_departure"],
                    'duration':response[0]["duration"],
                    'price':response[0]["price"],
                    'conversion':response[0]["conversion"],
                }

            print(f"City searched: {city['city']}, results finded: {len(response)}")
            
            if len(response) > 0:
                cheapers_flights.append({
                    "city":city["city"],
                    "total flights finded":len(response),
                    "flight":data,
                })

        print("\n")
        # pprint(cheapers_flights)
        # search the cheapest flight
        cheapest_flight = None
        for flight in cheapers_flights:
            if cheapest_flight is None:
                if flight["total flights finded"] > 0:
                    cheapest_flight = flight
                else:
                    continue
            elif flight["total flights finded"] > 0:
                if flight["flight"]["price"] < cheapest_flight["flight"]["price"]:
                    cheapest_flight = flight

        msg = f"Fly from {cheapest_flight['city']}-{cheapest_flight['flight']['flyFrom']}"    
        msg += f" to {cheapest_flight['flight']['cityTo']}-{cheapest_flight['flight']['flyTo']}"
        print(f"\nCHEAPEST FLIGHT, FINDED! :)\n{msg}\n\n")

        return {"cheapest_flight":cheapest_flight,"cheapers_flights":cheapers_flights}

    def __send_notification_by_SMS(self,cheapest_flight:dict) -> str:
        """Send a notification by SMS"""
        if cheapest_flight is not None:
            notification = NotificationManager()
            msg = "Low price alert!\n"
            msg += f"Fly from {cheapest_flight['city']}-{cheapest_flight['flight']['flyFrom']}"
            msg += f" to {cheapest_flight['flight']['cityTo']}-{cheapest_flight['flight']['flyTo']}"

            countries_data = [cheapest_flight['flight']['countryFrom'],cheapest_flight['flight']['countryTo']]
            msg += f", country from {countries_data[0]['name']}-{countries_data[0]['code']}"
            msg += f" contry to {countries_data[1]['name']}-{countries_data[1]['code']}"

            price_data = cheapest_flight['flight']['conversion']
            msg += f", {list(price_data.keys())[0]} {list(price_data.values())[0]}"

            msg += f", date: local arrival {cheapest_flight['flight']['local_arrival']}"
            msg += f", utc arrival {cheapest_flight['flight']['utc_arrival']}"
            msg += f", local departure {cheapest_flight['flight']['local_departure']}."
    
            notification.sendMsg(msg)

    def __fligth_str(self,fl) -> str:
        fligth = dict(fl)
        price_data = fligth['conversion']
        price_str = ""

        for k,v in price_data.items():
            price_str+=f"{k} {v}"

        msg = ""
        msg += f"\nFly from {fligth['flyFrom']} to {fligth['flyTo']},"
        msg += f"\ncity from {fligth['cityFrom']}-{fligth['cityCodeFrom']} to {fligth['cityTo']}-{fligth['cityCodeTo']},"
        msg += f"\ncountry from {fligth['countryFrom']['name']}-{fligth['countryFrom']['code']} to {fligth['countryTo']['name']}-{fligth['countryTo']['code']},"
        msg += f"\n"
        msg += f"\nDate: local arrival {fligth['local_arrival']}, utc arrival{fligth['utc_arrival']}, local departure{fligth['local_departure']}"
        msg += f"\n"
        msg += f"\nPrice: {price_str}"
        return msg

    def send_mails_to_customers(self):
        fligths = self.search_fligths()
        cheapest_flight = self.__fligth_str(fligths["cheapest_flight"]["flight"])

        cheapers_flights = []
        for f in list(fligths["cheapers_flights"]):
            cheapers_flights.append(self.__fligth_str(f["flight"]))

        flights_str = {"cheapest_flight":cheapest_flight,"cheapers_flights":cheapers_flights}
        mailManager = MailManager()
        mailManager.send_mail(self.customers,flights_str)
