from helpers import (
    create_trip,
    exit_program,
    my_travels,
    trips_by_country,
    trips_by_stars,
    trips_by_state,
    update_month,
    update_year,
    update_stars,
    update_all,
    remove,
    all_friends_visits,
    older_friends,
    younger_friends,
    sort_by_year,
    sort_by_name,
    sort_by_state,
    sort_by_country,
    update_name,
    reset_all,
    sort_by_month
)

def menu():
    print("Please select an option (enter number correspoding with menu item):\n")
    print("1. Where have you been? (Your travels)")
    print("2. Where have your friends been? (Friends' travels)")
    print("3. Show all travels (you and friends)")
    print("4. Update your name and age.")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        user_menu()
    elif choice == "2":
        friends_menu()
    elif choice == "3":
        show_all_loc_menu()
    elif choice == "4":
        update_name()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def user_menu():
    print("\nAdd your travels to the database or check out travels by you and your friends.\n")
    print("1. Enter a record of a location you've been to")
    print("2. Show locations you've been to using sorting/filtering options")
    print("3. Show all locations (both your friends' and yours).")
    print("4. Go back to prior menu")
    print("5. Reset all tables (removes information)")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "1":
        create_trip()
    elif choice == "2":
        show_locations_menu()
    elif choice == "3":
        show_all_loc_menu()
    elif choice == "4":
        menu()  
    elif choice == "5":
        print("\n Resetting will remove all data. There is NO turning back. \n Are you sure you want to remove data? \n")
        confirmation = input("Y/N:> ")
        if confirmation == "Y":
            reset_all()        
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def show_locations_menu():
    print("\nSelect how you'd like to review your travels\n")
    print("1. Show ALL locations you've been to.")
    print("2. Show locations you've been to BY COUNTRY.")
    print("3. Show locations you've been to BY STATE")
    print("4. Show locations you've been to with X NUMBER OF STARS")
    print("5. Update a location you've been to BY TRIP ID")
    print("6. Remove a location you've been to.")
    print("7. Go back to prior menu")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "1":
        my_travels()
    elif choice == "2":
        try:
            trips_by_country()
        except:
            print("\n No trips by country recorded \n")
    elif choice == "3":
        try:
            trips_by_state()
        except:
            print("\n No trips by state recorded \n")
    elif choice == "4":
        try:
            trips_by_stars()
        except:
            print("\n No trips by stars recorded \n")
    elif choice == "5":
        user_trip_update()
    elif choice == "6":
        remove()
    elif choice == "7":
        user_menu()    
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def show_all_loc_menu():
    print("\nSelect how you'd like to review ALL travels (yours and your friends'!)\n")
    print("1. Show ALL places, sorted by visit month (desc)")
    print("2. Show ALL places, sorted by visit year (desc)")
    print("3. Show ALL places, sorted alphabetically by name")
    print("4. Show ALL places,sorted alphabetically by state.")
    print("5. Show ALL places, sorted alphabetically by country.")
    print("6. Go back to prior menu")
    print("7. Reset all tables (removes information)")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "1":
        try:
           sort_by_month()
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "2":
        try:
            sort_by_year()
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "3":
        try:
            sort_by_name()
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "4":
        try:
            sort_by_state()
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "5":
        try:
            sort_by_country
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "6":
        user_menu()
    elif choice == "7":
        print("\n Resetting will remove all data. There is NO turning back. \n Are you sure you want to remove data? \n")
        confirmation = input("Y/N:> ")
        if confirmation == "Y":
            reset_all()
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def friends_menu():
    print("\nSelect how you'd like to review your FRIENDS' travels\n")
    print("1. Where have your friends been?")
    print("2. Where have friends older than you been?")
    print("3. Where have friends younger than you been?")
    print("4. Go back to prior menu")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "1":
        try:
            all_friends_visits()
        except:
            print("\n Friends do not have any visits. Have them add some! \n")
    elif choice == "2":
        try:
            older_friends()
        except:
            print("\n Friends do not have any visits. Have them add some! \n")
    elif choice == "3":
        try:
            younger_friends()
        except:
            print("\n Friends do not have any visits. Have them add some! \n")
    elif choice == "4":
        menu()
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to the menu item")

def user_trip_update():
    print("\nUpdate a record\n" + "Note: You must have the associated TripID! Enter '5' to get list of all trips.\n")
    print("1. Update month")
    print("2. Update year")
    print("3. Update stars")
    print("4. Update all")
    print("5. See all trips")
    print("6. Go back to prior menu")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "1":
        update_month()
    elif choice == "2":
        update_year()
    elif choice == "3":
        update_stars()
    elif choice == "4":
        update_all()
    elif choice == "5":
        my_travels()
    elif choice == "6":
        show_locations_menu()    
    elif choice == "0":
        exit_program()
    elif choice == "4":
        pass
        print("Invalid choice -- enter number corresponding to menu item")
