"""
* APIs Required
*   Google Sheet Data Management - https://sheety.co/
*   Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/
*   Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
*   Twilio SMS API - https://www.twilio.com/docs/sms
"""
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

from pprint import pprint

def main():
    data = DataManager()
    fl_search = FlightSearch()
    flight_data = FlightData()
    
    # get cities from sheete
    cities = data.get()
    # search and save IATA code
    codesSearched = 0
    for city in cities:
        if city["iataCode"] == "":
            IATA_code = fl_search.search_Country(city["city"])
            pprint(f"country:{city['city']} IATA_CODE:{IATA_code}")
            data.put(city["id"],city["city"],IATA_code,city["lowestPrice"])
            pprint("Data saved!")
            codesSearched+=1
    if codesSearched == 0:
        print("All cities are with IATA code!")
    print(f"Cities IATA code searched: {codesSearched}...\n")
            
    # search cheapers flights
    cheapers_flights = []
    for city in cities:
        response = flight_data.search_flights(city["iataCode"],f"{city['lowestPrice']}")["data"]
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
    
    print("\nCHEAPEST FLIGHT:\n\n",cheapest_flight)

    # send notifications by SMS
    if cheapest_flight is not None:
        notification = NotificationManager()
        
        msg = "Low price alert!\n"
        # The SMS should include the 
        # departure airport IATA code, 
        city_from = f"to fly from {cheapest_flight['city']}-{cheapest_flight['flight']['flyFrom']}"
        # destination airport IATA code, 
        city_to = f"to {cheapest_flight['flight']['cityTo']}-{cheapest_flight['flight']['flyTo']}"
        # departure city,
        countries_data = [cheapest_flight['flight']['countryFrom'],cheapest_flight['flight']['countryTo']]
        # 0 =  country From, 1 = country to
        country_from = f"contry from {countries_data[0]['name']}-{countries_data[0]['code']}"
        # destination city, 
        country_to = f"contry to {countries_data[1]['name']}-{countries_data[1]['code']}"
        # flight price
        price_data = cheapest_flight['flight']['conversion']
        price_str = f"{list(price_data.keys())[0]} {list(price_data.values())[0]}"
        # flight dates
        flight_date = f"date: local arrival {cheapest_flight['flight']['local_arrival']}"
        flight_date += f", utc arrival {cheapest_flight['flight']['utc_arrival']}"
        flight_date += f", local departure {cheapest_flight['flight']['local_departure']}"
        
        msg += f"{city_from} {city_to}, {country_from} {country_to}, price {price_str}, {flight_date}"
        notification.sendMsg(msg)

main()