import json
import os.path

def displayAllCars(cars):
    print("")
    for current_car in cars:
        for current_key in current_car:
            print(current_key, ":", current_car[current_key])

def getNumericInput(displayString):
    while(True):
        user_data = input(displayString)
        if(user_data.isnumeric()):
            user_data = int(user_data)
            return user_data
        else:
            print("please insert a number")

def addCar():
    car = {
            "template" : {
                "car_types" : [
                    "sedan",
                    "SUV",
                    "hatchback",
                    "racing",
                    "coupe",
                    "minivan",
                    "pickup"
                ],
                "year_of_production" : 0,
                "year_of_purchase" : 0,
                "mark" : "",
                "model" : "",
                "volume_of_engine" : 0,
                "power_source" : [
                    "fuel",
                    "electricity",
                    "disel",
                    "gas"
                ],
                "tank" : 0,
                "fuel_consumption" : 0,
                "metric" : [
                    "mile",
                    "km"
                    ]
                } ,
            }
    car["car_types"] = input("Please insert the car type: ")
