from helpers import (
    create_trip,
    exit_program,
    travels_by_name,
    trips_by_country,
    trips_by_stars,
    trips_by_state,
    update_month,
    update_year,
    update_stars,
    update_all,
    all_friends_visits
)

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Where have you been?")
    print("2. Where have your friends been?")
    print("3. Show all travels (you and friends)")

def user_menu():
    print("1. Enter a record of a location you've been to")
    print("2. Show locations you've been to.")
    print("3. Show all locations (both your friends' and yours).")
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
    print("4. Show locations I've been to with X number of stars")
    print("5. Update a location I've been to by trip ID")
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
        user_trip_update()
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def show_all_loc_menu():
    print("1. Show ALL places (unordered)")
    print("2. Sort by date of visit.")
    print("3. Sort alphabetically by name")
    print("4. Sort alphabetically by state.")
    print("5. Sort alphabetically by country.")
    choice = input("> ")
    if choice == 1:
        from trip import Trip
        Trip.get_all_by_visit()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 0:
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item") 

def friends_menu():
    print("1. Where have your friends been? THIS WILL GIVE ALL (minus you).")
    print("2. Where have friends older than you been?")
    print("3. Where have friends younger than you been?")
    print("4. How many friends have been to where I've been?")
    choice = input("> ")
    if choice == "1":
        all_friends_visits()
        pass
    elif choice == "2":
        #older friends
        pass
    elif choice == "3":
        #younger friends
        pass
    elif choice == "4":
        #same places
        pass
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to the menu item")

def user_trip_update():
    print("1. Update month")
    print("2. Update year")
    print("3. Update stars")
    print("4. Update all")
    choice = input("> ")
    if choice == 1:
        update_month()
    elif choice == 2:
        update_year()
    elif choice == 3:
        update_stars()
    elif choice == 4:
        update_all()
    elif choice == 0: 
        exit_program()
    elif choice == 4:
        pass
    else:
        print("Invalid choice -- enter number corresponing to menu item")              