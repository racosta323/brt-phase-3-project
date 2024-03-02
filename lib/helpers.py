from cli import main
from trip import Trip

def greeting():
    name = input("What is your name? ")
    age = input("How old are you? ")
    print(f'Hello, {name}! Nice to meet you.')

        
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
        enter_location()
    if choice == "2":
        pass

def enter_location():    
    print("What city have you been to? (Enter a location.)")
    city = input("> ")
    print("In what state?")
    state = input("> ")
    print("Out of 5, how many stars would you give it? (1: Meh to 5:Yeah!)")
    stars = input("> ")
    print("Cool. Thanks. Your entry has been recorded.")
    main()

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