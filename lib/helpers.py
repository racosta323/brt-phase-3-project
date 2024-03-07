import ipdb
from trip import Trip
from location import Location
from traveler import Traveler

travelers = {}
name_list = []
age_list = []

def greeting():
    print("\n   Welcome! Tell us where you've been or check out where your friends have been!\n    Enter your basic info to see menu options. (Enter 0 anytime to exit.)\n")
    name = input("What is your name?> ")
    if name == "0":
        exit_program()
    age = int(input("How old are you?> "))
    if age == 0:
        exit_program()
    print(f'\n  Hello, {name}! Nice to meet you.\n')
    try:
        traveler = Traveler.find_by_name(name.capitalize())
        travelers[traveler.id] = traveler
    except:
        traveler = Traveler.create_instance(name.capitalize(),age)
        travelers[traveler.id] = traveler
    name_list.append(name)
    age_list.append(age)
    

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
    print("\n   Enter basic trip details. \n" + "   Enter 'N/A' if not applicable or unsure.\n")
    city_input = input("What city have you been to? (Enter a location.)> ")
    if city_input == "0":
        exit_program()
    state = input("In what state?> ")
    if state == "0":
        exit_program()
    country = input("In what country?> ")
    if country == "0":
        exit_program()
    stars = input("Out of 5, how many stars would you give it? (1: Meh to 5:Yeah!)> ")
    if stars == "0":
        exit_program()
    if stars == "N/A":
        stars = 0
    year = input("What year did you go?> ")
    if year == "N/A":
        year = 0
    if year == "0":
        exit_program()
    month = input("In what month?> ")
    if month == "0":
        exit_program()
    name = name_list[-1]
    traveler = Traveler.find_by_name(name.capitalize())
    traveler_id = traveler.id
    try:
        location = Location.find_by_city(city_input)
        location_id = location.id
    except:
        location = Location.create_instance(city_input, state, country)
        location_id = location.id
    try:
        trip = Trip.create_instance(month, int(year), int(stars), location_id, traveler_id)
        print("\n Cool. Thanks. Your entry has been recorded. \n")
        return trip
    except Exception as exc:
        print("Error creating trip: ", exc)
    
def my_travels():    
    name = name_list[-1]
    travels = Traveler.get_all_travels_by_name(name.capitalize())
    if travels:
        results = [f'<trip_id: {travels[0]}, ity: {travels[1]}, state: {travels[2]}, country: {travels[3]}, month: {travels[4]}, year: {travels[5]}, stars_given: {travels[6]}>' for travels in travels]
        return results
    else:
        print("\n No data. \n Enter a trip through the 'Where have you been?' menu to create table.\n")

def update_name():
    name = name_list[-1]
    traveler = Traveler.find_by_name(name.capitalize())
    age = traveler.age
    print(f"\nYour name is currently {name}.")
    print(f"Your age is currently {age}.\n")
    updated_name = input("Enter your updated name:> ")
    updated_age = int(input("Enter your updated age:> "))
    traveler.name = updated_name.capitalize()
    traveler.age = updated_age
    try:
        traveler.update_in_db()
        print(f"\nYour name has updated to '{traveler.name}' \n Your age has updated to '{traveler.age}'.\n")
    except:
        print("Something went wrong. Update incomplete. Please try again.")

def trips_by_stars():
    name = name_list[-1]
    travels = Traveler.get_all_travels_by_name(name.capitalize())
    stars = int(input("Enter number of stars:> "))
    trips = [travel for travel in travels if travel[6] == stars]
    if trips:
        results = [f'<trip_id: {travels[0]}, city: {travels[1]}, state: {travels[2]}, country: {travels[3]}, month: {travels[4]}, year: {travels[5]}, stars_given: {travels[6]}>' for travels in travels]
        return results
    else:
        print(f"No matching entries with {stars} stars.\n")

def trips_by_country():
    name = name_list[-1]
    travels = Traveler.get_all_travels_by_name(name.capitalize())
    country = input("Enter country:> ")
    trips = [travel for travel in travels if travel[3] == country]
    if trips:
        results = [f'<trip_id: {travels[0]}, city: {travels[1]}, state: {travels[2]}, country: {travels[3]}, month: {travels[4]}, year: {travels[5]}, stars_given: {travels[6]}>' for travels in travels]
        return results
    else:
        print(f"No matching entries for {country}")

def trips_by_state():
    name = name_list[-1]
    travels = Traveler.get_all_travels_by_name(name.capitalize())
    state = input("Enter state:> ")
    trips = [travel for travel in travels if travel[2] == state]
    if trips:
        results = [f'<trip_id: {travels[0]}, city: {travels[1]}, state: {travels[2]}, country: {travels[3]}, month: {travels[4]}, year: {travels[5]}, stars_given: {travels[6]}>' for travels in travels]
        return results
    else:
        print(f"No matching entries for {state}")

def update_month():
    trip_id = int(input("Enter the trip_id for the trip you'd like to update:> "))
    month = input("What month would you like to update to?> ")
    trip = Trip.find_by_id(trip_id)
    trip.month = month
    trip.update_row()
    print(f"Updated month of trip_id: {trip_id} to {month}\n")

def update_year():
    trip_id = input("Enter the trip_id for the trip you'd like to update:> ")
    year = input("What year would you like to update to?> ")
    trip = Trip.find_by_id(trip_id)
    trip.year = year
    trip.update_row()
    print(f"Updated year of trip_id: {trip_id} to {year}\n")

def update_stars():
    trip_id = input("Enter the trip_id for the trip you'd like to update:> ")
    stars = input("How many stars would you like to update to?> ")
    trip = Trip.find_by_id(trip_id)
    trip.stars = stars
    trip.update_row()
    print(f"Updated stars of trip_id:{trip_id} to {stars}\n")

def update_all():
    trip_id = input("Enter the trip_id for the trip you'd like to update:> ")
    month = input("What month would you like to update to?> ")
    year = input("What year would you like to update to?> ")
    stars = input("How many stars would you like to update to?> ")
    trip = Trip.find_by_id(trip_id)
    trip.month = month
    trip.year = year
    trip.stars = stars
    trip.update_row()
    print(f"Updated month, year, stars for trip_id: {trip_id} to {month}, {year}, {stars}, respectively\n")

def remove():
    trip_id = input("Enter the trip_id for the trip you'd like to remove:> ")
    trip = Trip.find_by_id(trip_id)
    trip.destroy()    

def sort_by_month():
    trips = Trip.get_all_by_visit()
    sorted_trips = sorted(trips, key = lambda x: x[4], reverse=True)
    if sorted_trips:
        results = [f'<name: {travels[0]}, city: {travels[1]}, state: {travels[2]}, country: {travels[3]}, month: {travels[4]}, year: {travels[5]}, stars_given: {travels[6]}>' for travels in sorted_trips]
        return results
    else:
        print("No entries to display.")

def sort_by_year():
    trips = Trip.get_all_by_visit()
    sorted_trips = sorted(trips, key = lambda x: x[5], reverse=True)
    if sorted_trips:
        results = [f'<name: {travels[0]}, city: {travels[1]}, state: {travels[2]}, country: {travels[3]}, month: {travels[4]}, year: {travels[5]}, stars_given: {travels[6]}>' for travels in sorted_trips]        
        return results
    else:
        print("No entries to display.")

def sort_by_name():
    trips = Trip.get_all_by_visit()
    sorted_trips = sorted(trips, key = lambda x: x[0])
    if sorted_trips:
        results = [f'<name: {travels[0]}, city: {travels[1]}, state: {travels[2]}, country: {travels[3]}, month: {travels[4]}, year: {travels[5]}, stars_given: {travels[6]}>' for travels in sorted_trips]
        return results
    else:
        print("No entries to display.")

def sort_by_state():
    trips = Trip.get_all_by_visit()
    sorted_trips = sorted(trips, key = lambda x: x[2])
    if sorted_trips:
        results = [f'<name: {travels[0]}, city: {travels[1]}, state: {travels[2]}, country: {travels[3]}, month: {travels[4]}, year: {travels[5]}, stars_given: {travels[6]}>' for travels in sorted_trips]
        print("No entries to display.")

def sort_by_country():
    trips = Trip.get_all_by_visit()
    sorted_trips = sorted(trips, key = lambda x: x[3])
    if sorted_trips:
        results = [f'<name: {travels[0]}, city: {travels[1]}, state: {travels[2]}, country: {travels[3]}, month: {travels[4]}, year: {travels[5]}, stars_given: {travels[6]}>' for travels in sorted_trips]
        return results
    else:
        print("No entries to display.")

def all_friends_visits():
    name = name_list[-1]
    visits = [trip for trip in Trip.get_all_by_visit() if trip[0] != name.capitalize()]
    if not visits:
       print("\n Friends do not have any visits. Have them add some! \n")
    else:
        return visits

def older_friends():
    name = name_list[-1]
    age = age_list[-1]
    visits = [trip for trip in Trip.older_friends(age) if trip[0] != name.capitalize()]
    return visits

def younger_friends():
    name = name_list[-1]
    age = age_list[-1]
    visits = [trip for trip in Trip.younger_friends(age) if trip[0] != name.capitalize()]
    return visits
    
def reset_all():
    Location.reset()
    Trip.reset()
    Traveler.reset() 
    print("\n DATA HAS BEEN REMOVED \n")

ipdb.set_trace()