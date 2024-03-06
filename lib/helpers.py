import ipdb
# from cli import main
from trip import Trip
from location import Location
from traveler import Traveler
# from menus import menu

travelers = {}
name_list = []
age_list = []
traveler_id =""

def greeting():
    print("Welcome! Enter your details to see menu options. (Enter 0 anytime to exit.)")
    name = input("What is your name? ")
    if name == "0":
        exit_program()
    age = int(input("How old are you? "))
    if age == 0:
        exit_program()
    print(f'Hello, {name}! Nice to meet you.')
    try:
        traveler = Traveler.find_by_name(name)
        travelers[traveler.id] = traveler
    except:
        traveler = Traveler.create_instance(name,age)
        travelers[traveler.id] = traveler
    name_list.append(name)
    age_list.append(age)
    return name, age

def exit_program():
    print("Until next time, Traveler!")
    exit()

def create_trip():
    Trip.create_table()
    try:
        Traveler.get_all_from_db()
        Trip.get_all_from_db()
        Location.get_all_from_db()
    except:
        pass
    city_input = input("What city have you been to? (Enter a location.)> ")
    state = input("In what state?> ")
    country = input("In what country?> ")
    stars = int(input("Out of 5, how many stars would you give it? (1: Meh to 5:Yeah!)> "))
    year = int(input("What year did you go?> "))
    month = input("In what month?> ")
    name = name_list[-1]
    traveler = Traveler.find_by_name(name)
    traveler_id = traveler.id
    try:
        location = Location.find_by_city(city_input)
        location_id = location.id
    except:
        location = Location.create_instance(city_input, state, country)
        location_id = location.id
    try:
        trip = Trip.create_instance(month, year, stars, location_id, traveler_id)
        print("Cool. Thanks. Your entry has been recorded.")
        return trip
        # menu()
    except Exception as exc:
        print("Error creating trip: ", exc)
    
def my_travels():    
    name = name_list[-1]
    try:
        Traveler.get_all_travels_by_name(name)
    except:
        "No data - enter a location first"

def update_name():
    name = name_list[-1]
    traveler = Traveler.find_by_name(name)
    age = traveler.age
    print(f"Your name is currently {name}.")
    print(f"Your age is currently {age}.")
    updated_name = input("Enter your updated name:> ")
    updated_age = int(input("Enter your updated age:> "))
    traveler.name = updated_name
    traveler.age = updated_age
    traveler.update_row()
    print(f"Your name has updated to '{traveler.name}' \n Your age has updated to '{traveler.age}'.")

def trips_by_stars():
    stars = input("Enter number of stars:> ")
    print([travel for travel in my_travels() if travel[6] == int(stars)])

def trips_by_country():
    country = input("Enter country:> ")
    print([travel for travel in my_travels() if travel[3] == country])

def trips_by_state():
    state = input("Enter state:> ")
    print([travel for travel in my_travels() if travel[2] == state])

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

def remove():
    trip_id = input("Enter the trip ID for the trip you'd like to remove:> ")
    trip = Trip.find_by_id(trip_id)
    trip.destroy()    

def sort_by_year():
    trips = Trip.get_all_by_visit()
    sorted_trips = sorted(trips, key = lambda x: x[5])
    print(sorted_trips)
    return sorted_trips

def sort_by_name():
    trips = Trip.get_all_by_visit()
    sorted_trips = sorted(trips, key = lambda x: x[0])
    print(sorted_trips)
    return sorted_trips

def sort_by_state():
    trips = Trip.get_all_by_visit()
    sorted_trips = sorted(trips, key = lambda x: x[2])
    print(sorted_trips)
    return sorted_trips

def sort_by_country():
    trips = Trip.get_all_by_visit()
    sorted_trips = sorted(trips, key = lambda x: x[3])
    print(sorted_trips)
    return sorted_trips

def all_sorted_by_visit():
    Trip.get_all_by_visit()

def all_friends_visits():
    name = name_list[-1]
    visits = [trip for trip in Trip.get_all_by_visit() if trip[0] != name]
    return visits

def older_friends():
    name = name_list[-1]
    age = age_list[-1]
    visits = [trip for trip in Trip.older_friends(age) if trip[0] != name]
    return visits

def younger_friends():
    name = name_list[-1]
    age = age_list[-1]
    visits = [trip for trip in Trip.younger_friends(age) if trip[0] != name]
    return visits
    
def reset_all():
    Location.reset()
    Trip.reset()
    Traveler.reset()    

# def same_places():
#     my = my_travels()
#     friends = all_friends_visits()
#     for travel in my:
#         if travel[1] in :
    

# ipdb.set_trace()
