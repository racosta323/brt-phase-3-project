from helpers import (
    create_trip,
    show_locations_menu,
    show_all_loc_menu,
    exit_program,
    travels_by_name,
    trips_by_country,
    trips_by_stars,
    trips_by_state
)

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Where have you been?")
    print("2. Where have your friends been?")
    print("3. Show all travels (you and friends)")

def user_menu():
    print("1. Enter a record of a location you've been to")
    print("2. Show locations I've been to.")
    print("3. Show all locations (both my friends and me).")
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

def show_locations_menu():
    print("1. Show all locations I've been to.")
    print("2. Show locations I've been to by country.")
    print("3. Show locations I've been to by state.")
    print("4. Show locations I've been to with X stars")
    print("5. Update a location I've been to.")
    choice = input("> ")
    if choice == "1":
        travels_by_name()
    elif choice == "2":
        trips_by_country()
    elif choice == "3":
        trips_by_state()
    elif choice == "4":
        trips_by_stars()
    elif choice == "5":
        pass
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def show_all_loc_menu():
    print("1. Show all places I've been to")
    print("2. Sort by date of visit.")
    print("3. Sort alphabetically by state.")
    print("4. Sort alphabetically by country.")
    choice = input("> ")
    if choice == 1:
        from trip import Trip
        Trip.get_all_by_visit()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 0:
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item") 

def friends_menu():
    print("Where have your friends been? THIS WILL GIVE ALL.")
    print("Where have friends older than you been?")
    print("Where have friends younger than you been?")
    print("How many friends have been to where I've been?")                 