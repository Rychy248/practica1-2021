class Car():
    def __init__(self,**kwargs):
        self.model = kwargs.get("model") #get() return the value if the key exist, kwargs["model"]
        self.make = kwargs.get("make") # if the key doesn't exist return none, its similar to > kwargs["make"]
                    #But the diference is, don't give us an error

my_car1 = Car(make="Nissan",model="GT-R")
print("Make: ",my_car1.make,", Model: ",my_car1.model)
my_car2 = Car()
print("Make: ",my_car2.make,", Model: ",my_car2.model)
