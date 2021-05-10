import json

def displayAllCars(cars):
    for current_car in cars:
        for current_key in current_car:
            return current_car[current_key]

def getNumericInput(displayString):
    while(True):
        user_data = input(displayString)
        if(user_data.isnumeric()):
            user_data = int(user_data)
            return user_data
        else:
            print("please insert a number")

def addCar():
    
    with open('cardash.json') as file_data:
        print(file_data)
        car = json.load(file_data)
        car["car_types"] = input("Please insert the car type: ")
        car["year_of_production"] = getNumericInput("Please insert the year of production:")
        car["year_of_purchase"] = getNumericInput("Please insert the year of purchase:")
        car["mark"] = input("Please insert the mark of the car:")
        car["model"] = input("Please insert the model of the car:")
        car["volume_of_engine"] = getNumericInput("Please insert the engine volume of the car:")
        car["power_source"] = input("please insert the power source: fuel, gas, diesel or electricity:")
        car["tank"] = getNumericInput("please insert the volume of the tank in liters:")
        car["fuel_consumption"] = getNumericInput("please insert the power source consumption per 100km:")
        car["metric"] = input("km or miles:")
        car["distance"] = getNumericInput ("please insert how much distance did you drive: ")
        car["fuel_left"] = getNumericInput ("please tell how much fuel is left: ")
        car["distance_left"] = 0
    return car

def loadExistingCars():
    with open('cars.json') as file_data:
        print(file_data)
        cars = json.load(file_data)
        return cars

def saveToTheFile(cars):
    f = open("cars.json", "w")
    f.write(json.dumps(cars, indent = 2))
    f.close

def main():
    print("Welcome to the CarDash, we want to help you about your car usage status after you give some important details about it.")

    cars = []

    cars = loadExistingCars()

    while(True):
        insert_mode = input("Do you want to start adding cars? Please answer yes or no:")
        if(insert_mode == "no"):
            print("Goodbye, thank you for using CarDash")
            break
        else:
            car = addCar()
            cars.append(car)

    print("Saving to the file")
    saveToTheFile(cars)
    displayAllCars(cars)

main()




