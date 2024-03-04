import ipdb
# from cli import main
from trip import Trip
from location import Location
from traveler import Traveler

traveler = []
age_list = []
traveler_id =""

def greeting():
    print("Welcome! Enter your details to see menu options. (Enter 0 anytime to exit.)")
    name = input("What is your name? ")
    if name == "0":
        exit_program()
    age = input("How old are you? ")
    if age == "0":
        exit_program()
    print(f'Hello, {name}! Nice to meet you.')
    #add to travelers db (pending)
    traveler.append(name)
    age_list.append(age)
    return name, age
        
def exit_program():
    print("Until next time, Traveler!")
    exit()

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Where have you been?")
    print("2. Where have your friends been?")
    print("3. Show all travels (you and friends)")

def user_menu():
    print("1. Enter a record of a location you've been to")
    print("2. Show locations I've been to.")
    choice = input("> ")
    if choice == "1":
        create_trip()
    elif choice == "2":
        show_locations_menu()
    elif choice == "3":
        show_all_loc_menu()
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")    
           
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
    choice = input("> ")
    if choice == "1":
        travels_by_name()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")
    
def travels_by_name():    
    person = Traveler(traveler[0], 1, int(age_list[0]))
    Traveler.get_all_travels_by_name(person)

def show_all_loc_menu():
    print("1. Sort by date of visit.")
    print("2. Sort alphabetically by state.")
    print("3. Sort alphabetically by country.")
    

def friends_menu():
    print("Where have your friends been? THIS WILL GIVE ALL.")
    print("Where have friends older than you been?")
    print("Where have friends younger than you been?")
    print("How many friends have been to where I've been?")  