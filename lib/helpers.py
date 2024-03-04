import ipdb
# from cli import main
from trip import Trip
from location import Location
from traveler import Traveler

name = ""
age = ""
traveler_id =""

def greeting():
    name = input("What is your name? ")
    age = input("How old are you? ")
    print(f'Hello, {name}! Nice to meet you.')
    return name, age
        
def exit_program():
    print("Until next time, Traveler!")
    exit()

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Where have you been?")
    print("2. Where have your friends been?")

def user_menu():
    print("1. Enter a record of a location you've been to")
    print("2. Show my locations.")
    choice = input("> ")
    if choice == "1":
        create_trip()
    if choice == "2":
        pass

def create_trip():
    Trip.create_table()    
    city = input("What city have you been to? (Enter a location.)> ")
    state = input("In what state?> ")
    country = input("In what country?> ")
    stars = int(input("Out of 5, how many stars would you give it? (1: Meh to 5:Yeah!)> "))
    year = int(input("What year did you go?> "))
    month = input("In what month?> ")
    try:
        location = Location(city, state, country, 1)
        tr1 = Traveler("Rene", 1, 35)
        tr2 = Traveler("Keya", 2, 25)
        trip = Trip.create_instance(month, year, stars, location.id, 1)
        print("Cool. Thanks. Your entry has been recorded.")
    except Exception as exc:
        print("Error creating trip: ", exc)

def show_locations_menu():
    print("1. Show all locations I've been to.")
    print("2. Show locations I've been to by country.")
    print("3. Show locations I've been to by state.")
    print("4. Show locations I've been to with X stars")

def show_all_loc_menu():
    print("1. Sort by date of visit.")
    print("2. Sort alphabetically by state.")
    print("3. Sort alphabetically by country.")
    

def friends_menu():
    print("Where have your friends been? THIS WILL GIVE ALL.")
    print("Where have friends older than you been?")
    print("Where have friends younger than you been?")
    print("How many friends have been to where I've been?")  