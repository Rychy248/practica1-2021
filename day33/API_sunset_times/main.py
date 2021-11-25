import requests
from datetime import datetime as dt
try:
    import my_position as mp
except ModuleNotFoundError:
    with open("my_position.py","w") as file:
        file.write("#put your coordenates here\nMY_LAT = 0\nMY_LNG = 0")
    import my_position as mp

# API endpoint sunset rise time https://api.sunrise-sunset.org/json
# web https://sunrise-sunset.org/api

# Parameters
#     lat (float): Latitude in decimal degrees. Required.
#     lng (float): Longitude in decimal degrees. Required.
#     date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. If not present, date defaults to current date. Optional.
#     callback (string): Callback function name for JSONP response. Optional.
#     formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.
if mp.MY_LAT==0 and mp.MY_LNG==0:
    raise ValueError("Coordenates are wrong check the file 'my_position.py'")

parameters = {
    "lat":mp.MY_LAT,
    "lng":mp.MY_LNG,
    "formatted":0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status() #raise if exists for type error
data = response.json()
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0]) # gettin the hour only
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0]) # gettin the hour only

print(f"sunrise={sunrise}, sunset={sunset}")

time_now = dt.now()
print(time_now)