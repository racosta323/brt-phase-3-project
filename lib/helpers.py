import ipdb
# from cli import main
from trip import Trip
from location import Location
from traveler import Traveler
# from menus import menu

traveler = {}
age_list = []
traveler_id =""

def greeting():
    Traveler.get_all_from_db()
    print("Welcome! Enter your details to see menu options. (Enter 0 anytime to exit.)")
    name = input("What is your name? ")
    if name == "0":
        exit_program()
    for traveler in Traveler.all:
        if Traveler.all[traveler].name == name:
            print("name is here")    
    age = int(input("How old are you? "))
    if age == "0":
        exit_program()
    print(f'Hello, {name}! Nice to meet you.')
    traveler["name"] = name
    traveler["age"] = age
    return name, age
        
def exit_program():
    print("Until next time, Traveler!")
    exit()
              
def create_trip():
    Trip.create_table()    
    city = input("What city have you been to? (Enter a location.)> ")
    state = input("In what state?> ")
    country = input("In what country?> ")
    stars = int(input("Out of 5, how many stars would you give it? (1: Meh to 5:Yeah!)> "))
    year = int(input("What year did you go?> "))
    month = input("In what month?> ")
    try:
        location = Location.create_instance(city, state, country)
        trip = Trip.create_instance(month, year, stars, location.id, 1)
        print("Cool. Thanks. Your entry has been recorded.")
        # menu()
    except Exception as exc:
        print("Error creating trip: ", exc)
    
def travels_by_name():    
    person_name = traveler["name"]
    Traveler.get_all_travels_by_name(person_name)

def trips_by_stars():
    person = Traveler.create_instance(traveler["name"], int(traveler["age"]))
    stars = input("Enter number of stars:> ")
    ipdb.set_trace()
    person.trips_by_stars(stars)

def trips_by_country():
    person = Traveler.create_instance(traveler["name"], int(traveler["age"]))
    country = input("Enter name of country:> ")
    person.trips_by_country(country)   

def trips_by_state():
    person = Traveler.create_instance(traveler["name"], int(traveler["age"]))
    state = input("Enter the abbr. for the state:> ")
    person.trips_by_state(state)

def update_month():
    trip_id = input("Enter the trip ID for the trip you'd like to update:> ")
    month = input("What month would you like to update to?> ")
    trip = Trip.find_by_id(trip_id)
    trip.month = month
    trip.update_row()

def update_year():
    trip_id = input("Enter the trip ID for the trip you'd like to update:> ")
    year = input("What year would you like to update to?> ")
    trip = Trip.find_by_id(trip_id)
    trip.year = year
    trip.update_row()

def update_stars():
    trip_id = input("Enter the trip ID for the trip you'd like to update:> ")
    stars = input("How many stars would you like to update to?> ")
    trip = Trip.find_by_id(trip_id)
    trip.stars = stars
    trip.update_row()

def update_all():
    trip_id = input("Enter the trip ID for the trip you'd like to update:> ")
    month = input("What month would you like to update to?> ")
    year = input("What year would you like to update to?> ")
    stars = input("How many stars would you like to update to?> ")
    trip = Trip.find_by_id(trip_id)
    trip.month = month
    trip.year = year
    trip.stars = stars
    trip.update_row()
    

def all_sorted_by_visit():
    Trip.get_all_by_visit()

ipdb.set_trace()      