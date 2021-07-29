#PANDAS LIBRARY
#API Reference: https://pandas.pydata.org/docs/reference/index.html
#Documentation: https://pandas.pydata.org/docs/

""" H A R D - W A Y
with open("weather_data.csv") as csv_file:
    days = csv_file.readlines()
    index = 0
    for day in days[1:]: #a list of strings
        days[index] = (day.split()) #split create a list of words into list
        print(day.split())
        index+=1 
"""
""" M E D I U M - W A Y 
import csv

with open("weather_data.csv") as csv_file:
    #data = csv.reader(csv_file)
    #on this form, the result is a _csv.reader type object
    data=list(csv.reader(csv_file)) # convert the _csv.reader into a list
    index=0
    for row in data[1:]:
        data[index][1] = int(row[1])
        print(data[index][1])
        index+=1
"""

#"" I N T E L I G E N T - W A Y
import pandas #you need to install this library

data = pandas.read_csv("weather_data.csv")
print("",type(data),"\n___u.u___\n",data)
print("\n___u.u___\n",data["temp"])#in our csv file "weather_data.csv" the first line contenies the columns names
print("Avegare temp = ",data["temp"].mean())
print("Max. Temp = ",data["temp"].max(),"Min. Temp = ",data["temp"].min())
#the column can be specified by it's name or like an atribute
print("Avegare temp = ",data.temp.mean())

print("\n"*3)
#print(data[day.["day"] == "Monday"]) the next line is equal to this|
print(data[data.day == "Monday"],"'Monday data'")#HOW PRINT A COLUMN? here your answer
#the row how have the max temp
print(data[data.temp == data.temp.max()],"'The day who have the max temp'")
#you can acces into a column from a specifc column, like next
tuesday = data[data.day == "Tuesday"]
print("Tuesday: condition=",tuesday.condition," temp=",int(tuesday.temp)*9/5+32,"farengi")


