import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
#instaled librarys
from twilio.rest import Client
#own module
import API_KEYS as ak

# TSLA Stock Price https://www.tradingview.com/symbols/NASDAQ-TSLA/
# Twilio API https://www.twilio.com/
# News API https://newsapi.org/
# Alpha Vantage API https://www.alphavantage.co/

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

class StocPrice():
    def __init__(self):
        self.two_last_days_data = {}
        self.last_days=[] #dates as string of two last days
        self.avg_situation= 0.0

        self.__get_data()

    def __get_data(self):
        today = date.today()
        #three last days
        #last_days = [f"{today - timedelta(days=i)}" for i in range(1,4,1)]
        self.last_days=[]
        
        params = {
        "function":"TIME_SERIES_DAILY",
        "symbol":STOCK,
        "apikey":ak.ALPHA_AVANGE,
        }
        response = requests.get(url="https://www.alphavantage.co/query?",params=params)
        data = response.json()
        
        #two last days in returned data
        i = 1
        while len(self.last_days)<2 or i>=15:
            day_try = f"{today - timedelta(days=i)}"
            if day_try in data["Time Series (Daily)"]:
                self.last_days.append(day_try)
            i+=1

        self.two_last_days_data  = {day:{
            "open":float(data["Time Series (Daily)"][day]["1. open"]),
            "close":float(data["Time Series (Daily)"][day]["4. close"]),
            } for day in self.last_days}
        
        # refresh_situation of averange
        difference = self.two_last_days_data[self.last_days[0]]["close"] - self.two_last_days_data[self.last_days[1]]["close"]
        self.avg_situation = difference*100/self.two_last_days_data[self.last_days[0]]["close"]

        if self.avg_situation < 0:
            self.messegue = f"It's a bad situation ☹ for us, {STOCK} actions are decresed by 🔻{self.avg_situation}%"
        elif 0 < self.avg_situation < 5:
            self.messegue = f"Don't worry 😉, our money is safe, {STOCK} actions are in a lineal situation ➡{self.avg_situation}%"
        else:
            self.messegue = f"It's a great situation 🤑 for us, {STOCK} actions are incresed by ✅{self.avg_situation}%"
        self.messegue+=f"\nDates comparated {self.last_days[0]} with {self.last_days[1]}\n\n"


class News():
    def __init__(self,days:list):
        self.days = days
        self.news_list = {}
        self.news_str = ""
        self.__get_data()

    def __get_data(self):
        params = {
            "q":COMPANY_NAME,
            "pageSize":"3",
            "sortBy":"popularity",
            "apiKey":ak.NEWS_API,
            "from":self.days[1],
            "to":self.days[0],
        }
        response = requests.get(url="https://newsapi.org/v2/everything?",params=params)
        data = response.json()["articles"]

        for new in data:
            soup = BeautifulSoup(new['description'],'html.parser')
            self.news_list[new['title']]=soup.get_text()
            self.news_str+=f"---Headline: {new['title']}\n---new: {soup.get_text()}\n* * *\n"

        
class SendMessegueSMS():
    def __init__(self,messegue:str):
        account_sid = ak.ACOOUNT_SID
        auth_token = ak.AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                     body=messegue,
                     from_=ak.MY_NUMBER,
                     to='+50242090991'
                 )
        print("NOTIFICATION SENDED, message sid: ",message.sid)

def main():
    sp = StocPrice()
    print("STOCK prices getting...")
    news = News(sp.last_days)
    print("Getting news...")
    messegue = f"{sp.messegue}\nGetting news...\n{news.news_str}\n\nNotifyded by RychSystem :)"
    send_sms= SendMessegueSMS(messegue)

main()