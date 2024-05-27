import json
import os
from enum import Enum
from icecream import ic

cars = list([{'Type': 'audi', 'Model': 2022, 'Color': 'black'}])


class Actions(Enum):
    ADD = 1
    DELETE = 2
    PRINT = 3
    UPDATE = 4
    EXIT = 5
    INFO = 6
    RESET = 7


def menu():
    for action in Actions:
        print(f'{action.name} - {action.value}')
    return Actions(int(input("choose one from the above :")))
    

def print_cars():
    for index , car in enumerate(cars) :
        print(f'{index} {car["Type"]} , {car["Model"]} , {car["Color"]}')


def add_cars():
    cars.append({'Type' : input("Car type?") , 'Model' : input("Car model?") , 'Color' : input("Car color?")})


def find_cars():
    print_cars()
    which_car= int(input("choose which car to delete :"))
    return which_car

def del_cars():
    which_car= find_cars()
    print(f'{cars[which_car]} car has deleted')
    cars.pop(which_car)


def upd_cars():
     which_car= find_cars()
     cars[which_car] = {'Type': input("What is the car type? ") , 'Model': input("What is the car Model ") , 'Color': input("What is the car color? ")}


def count_cars():
    count = len(cars)
    print(f'There are {count} cars')

def load_cars_from_json(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump([], file)
    with open(filename, 'r') as file:
        cars = json.load(file)
    return cars


def save_cars_to_json(cars, filename):
    with open(filename, 'w') as file:
        json.dump(cars, file)


def restart(filename):
    global cars
    if os.path.exists(filename):
        os.remove(filename)
    cars.clear()



   

if __name__ == "__main__" :
    cars = load_cars_from_json('cars.json')
    while True:
        user_selection= menu()
        if user_selection== Actions.EXIT :
            save_cars_to_json(cars , 'cars.json')
            exit()
        if user_selection== Actions.PRINT : print_cars()
        if user_selection== Actions.ADD : add_cars()
        if user_selection== Actions.DELETE : del_cars()
        if user_selection== Actions.UPDATE : upd_cars()
        if user_selection== Actions.INFO : count_cars()
        if user_selection== Actions.RESET : restart('cars.json')
       