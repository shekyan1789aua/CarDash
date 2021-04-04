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
                    "diesel",
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
    car["year_of_production"] = getNumericInput("Please insert the year of production:")
    car["year_of_purchase"] = getNumericInput("Please insert the year of purchase:")
    car["mark"] = input("Please insert the mark of the car:")
    car["model"] = input("Please insert the model of the car:")
    car["volume_of_engine"] = getNumericInput("Please insert the engine volume of the car:")
    car["power_source"] = input("please insert the power source; fuel, gas, diesel or electricity:")
    car["tank"] = getNumericInput("please insert the volume of the tank in liters:")
    car["fuel_consumption"] = getNumericInput("please insert the fuel-consumption per 100km")
    car["metric"] = input("km or miles")
    car[""].append()
    return car

    
def loadExistingCars():
    if(os.path.exists("cardash.json")):
        with open('cardash.json') as file_data:
            print(file_data)
            cars = json.load(file_data)
            return cars
    else:
        return []

def saveToTheFile(cars):
    f = open("cardash.json", "w")
    f.write(json.dumps(cars, indent = 2))
    f.close

def main():

    cars = []
    cars = loadExistingCars()

    while(True):
        insert_mode = input("Do you want to start adding cars? please answer yes or no:")
        if(insert_mode == "no"):
            print("Bye")
            break
        else:
            cars = addCar()
            car[""].append()

    saveToTheFile(cars)
    displayAllCars(cars)

main()





